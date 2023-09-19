# coding: utf-8

from __future__ import absolute_import

import datetime
import os
import uuid

from datatransfer.common import constants
from datatransfer.common.constants import MODE_ALL
from datatransfer.common.constants import MODE_UPDATED
from datatransfer.source import configs as dt_settings
from datatransfer.source.catalog.tasks import save_feedback_result
from datatransfer.source.common.tasks import data_transfer_task
from datatransfer.source.transport.smev.datapush.models import DataPushRequest
from datatransfer.source.transport.smev.datapush.models import DataPushResponse
from datatransfer.source.transport.smev.datapush.models import FeedbackRequest
from datatransfer.source.transport.smev.datapush.models import FeedbackResponse

from dateutil import parser as date_parser
from spyne.decorator import rpc
from spyne.error import Fault


modes = {
    DataPushRequest.Mode.ALL: MODE_ALL,
    DataPushRequest.Mode.UPDATED: MODE_UPDATED
}


@rpc(DataPushRequest,
     _returns=DataPushResponse)
def DataPush(context, DataPushRequest):
    InMessage = context.udc.in_smev_message
    OutMessage = context.udc.out_smev_message

    response = DataPushResponse()

    response.SessionID = DataPushRequest.SessionID

    OutMessage.Service.Mnemonic = (
        dt_settings.SMEV_MNEMONICS)
    OutMessage.Service.Version = (
        constants.DATAPUSH_SERVICE_VERSION)
    OutMessage.Sender.Code = (
        dt_settings.SMEV_MNEMONICS)
    OutMessage.Sender.Name = (
        dt_settings.SMEV_NAME)
    OutMessage.TypeCode = (
        constants.SMEV_TYPE_CODE)

    try:
        if InMessage.Service.Mnemonic != dt_settings.SMEV_MNEMONICS:
            raise Fault(faultcode=u"INVALID", faultstring=u"Неизвестная мнемоника сервиса")

        if InMessage.Service.Version != constants.DATAPUSH_SERVICE_VERSION:
            raise Fault(faultcode=u"INVALID", faultstring=u"Некорректная версия сервиса")

        if InMessage.Recipient.Code != dt_settings.SMEV_MNEMONICS:
            raise Fault(faultcode=u"INVALID", faultstring=u"Неизвестный получатель")

        if not (InMessage.Sender.Code == dt_settings.DATATRANSFER_MNEMONICS
                and DataPushRequest.AuthorizationKey == dt_settings.DATAPUSH_AUTHORIZATION_KEY):
            raise Fault(faultcode=u"INVALID", faultstring=u"Неавторизованный запрос")

        if not InMessage.TestMsg:
            task = data_transfer_task.apply_async({}, {
                'session_id': DataPushRequest.SessionID,
                'method': 'DataTransfer',
                'mode': modes.get(DataPushRequest.Mode, MODE_ALL)
            })
            task_id = task.id
        else:
            task_id = str(uuid.uuid1())

        response.SessionID = response.SessionID or task_id
    except Fault as e:
        OutMessage.Status = e.faultcode
        response.Message = e.faultstring

    return response


@rpc(FeedbackRequest,
     _returns=FeedbackResponse)
def Feedback(context, FeedbackRequest):
    InMessage = context.udc.in_smev_message
    OutMessage = context.udc.out_smev_message

    response = FeedbackResponse()

    response.SessionID = FeedbackRequest.SessionID

    OutMessage.Service.Mnemonic = (
        dt_settings.SMEV_MNEMONICS)
    OutMessage.Service.Version = (
        constants.DATAPUSH_SERVICE_VERSION)
    OutMessage.Sender.Code = (
        dt_settings.SMEV_MNEMONICS)
    OutMessage.Sender.Name = (
        dt_settings.SMEV_NAME)
    OutMessage.TypeCode = (
        constants.SMEV_TYPE_CODE)

    try:
        if InMessage.Service.Mnemonic != dt_settings.SMEV_MNEMONICS:
            raise Fault(faultcode=u"INVALID", faultstring=u"Неизвестная мнемоника сервиса")

        if InMessage.Service.Version != constants.DATAPUSH_SERVICE_VERSION:
            raise Fault(faultcode=u"INVALID", faultstring=u"Некорректная версия сервиса")

        if InMessage.Recipient.Code != dt_settings.SMEV_MNEMONICS:
            raise Fault(faultcode=u"INVALID", faultstring=u"Неизвестный получатель")

        if not (InMessage.Sender.Code == dt_settings.DATATRANSFER_MNEMONICS
                and FeedbackRequest.AuthorizationKey == dt_settings.DATAPUSH_AUTHORIZATION_KEY):
            raise Fault(faultcode=u"INVALID", faultstring=u"Неавторизованный запрос")

        now = datetime.datetime.now()
        today = datetime.date.today()

        archive_path = os.path.join(
            dt_settings.STORAGE_MAILBOX_PATH,
            constants.CONFIGURATION_ARCHIVE_IN,
            str(today.year), str(today.month), str(today.day))

        AppDocument = context.udc.in_smev_appdoc
        archive_filename = os.path.join(
            archive_path,
            u"{0}_{1}_{2}.zip".format(
                InMessage.Sender.Code, AppDocument.RequestCode,
                now.strftime('%Y%m%d_%H%M%S')))

        try:
            if not os.path.exists(archive_path):
                os.makedirs(archive_path)

            with open(archive_filename, 'w+b') as decoded_file:
                decoded_file.write(
                    AppDocument.BinaryData.data[0])
        except Exception as e:
            raise Fault(faultcode=u"FAILURE", faultstring=u"Ошибка доступа к файлу: {0}".format(
                str(e)))

        if not InMessage.TestMsg:
            date_time_str = context.udc.in_smev_message_document.find(
                    "./{http://smev.gosuslugi.ru/rev120315}Date").text
            date_time = date_parser.parse(date_time_str)
            session = context.in_object.FeedbackRequest.SessionID

            save_feedback_result.apply_async((
                AppDocument.RequestCode,
                archive_filename,
                session,
                date_time
            ), kwargs={})
    except Fault as e:
        OutMessage.Status = e.faultcode
        response.Message = e.faultstring

    return response
