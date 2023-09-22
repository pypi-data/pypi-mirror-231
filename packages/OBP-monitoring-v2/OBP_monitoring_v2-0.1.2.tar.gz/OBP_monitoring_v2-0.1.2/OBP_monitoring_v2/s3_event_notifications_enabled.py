import logging

from botocore.exceptions import ClientError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


# checks the compliance.py for s3 bucket versioning enabled
def s3_event_notifications_enabled(self):
    """

    :param self:
    :return dict:
    """
    logger.info(" ---Inside OBP MMonitoring :: s3_event_notificationsenabled()")
    self.refresh_session()

    result = True
    failReason = ''
    offenders = []
    control_id = 'Id11.1'
    compliance_type = "S3 event notifications enabled"
    description = "Checks if Amazon S3 Events Notifications are enabled on an S3 bucket."
    resource_type = "S3 Buckets"
    risk_level = 'Medium'

    client = self.session.client('s3')
    try:
        response = client.list_buckets()
    except ClientError:
        result = False
        failReason = "Access denied for list buckets"
        offenders.append('')
    else:
        for bucket in response['Buckets']:
            bucket_name = bucket['Name']

            try:
                resp = client.get_bucket_notification_configuration(
                    Bucket=bucket_name,
                )
                #print(resp)
                del resp['ResponseMetadata']
                notifications_enabled = bool(resp)
                if notifications_enabled == False:
                    raise KeyError

            except KeyError:
                result = False
                failReason = "Notifications are turned off for S3 buckets."
                offenders.append(bucket_name)
                continue
            except ClientError:
                result = False
                failReason = "Access denied for get_bucket_logging api"
                offenders.append(bucket_name)

    return {
        'Result': result,
        'failReason': failReason,
        'resource_type': resource_type,
        'Offenders': offenders,
        'Compliance_type': compliance_type,
        'Description': description,
        'Risk Level': risk_level,
        'ControlId': control_id
    }
