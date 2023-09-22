import datetime

import boto3
import pytz
from boto3 import session
import logging

from botocore.exceptions import ClientError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

__author__ = 'Klera DevOps'
__version__ = '0.1.2'


class aws_client:
    def __init__(self, **kwargs):
        if 'aws_access_key_id' in kwargs.keys() and 'aws_secret_access_key' in kwargs.keys():
            if 'iam_role_to_assume' in kwargs.keys():
                self.iam_role_to_assume = kwargs['iam_role_to_assume']
                self.sts_client = boto3.client(
                    'sts',
                    aws_access_key_id=kwargs['aws_access_key_id'],
                    aws_secret_access_key=kwargs['aws_secret_access_key'],
                )
                self.creds = self.sts_client.assume_role(
                    RoleArn=self.iam_role_to_assume,
                    RoleSessionName='RecommenderSession',
                    DurationSeconds=3600
                )
                self.session = session.Session(
                    aws_access_key_id=self.creds['Credentials']['AccessKeyId'],
                    aws_secret_access_key=self.creds['Credentials']['SecretAccessKey'],
                    aws_session_token=self.creds['Credentials']['SessionToken']
                )
            else:
                self.session = session.Session(
                    aws_access_key_id=kwargs['aws_access_key_id'],
                    aws_secret_access_key=kwargs['aws_secret_access_key'],
                )
        elif 'profile_name' in kwargs.keys():
            self.session = session.Session(profile_name=kwargs['profile_name'])
        elif 'iam_role_to_assume' in kwargs.keys():
            self.iam_role_to_assume = kwargs['iam_role_to_assume']
            self.sts_client = boto3.client('sts')
            self.creds = self.sts_client.assume_role(
                RoleArn=kwargs['iam_role_to_assume'],
                RoleSessionName='RecommenderSession',
                DurationSeconds=3600
            )
            self.session = session.Session(
                aws_access_key_id=self.creds['Credentials']['AccessKeyId'],
                aws_secret_access_key=self.creds['Credentials']['SecretAccessKey'],
                aws_session_token=self.creds['Credentials']['SessionToken']
            )

    from .utils import get_regions, list_rds_clusters, list_ec2_instances, list_eni, list_security_groups, \
        list_lambda_functions, list_elbv2, list_auto_scaling_groups, list_as_launch_configs, list_elb
    from .rds import rds_cluster_iam_authentication_enabled
    from .ec2 import ec2_token_hop_limit_check, ec2_security_group_attached_to_eni, ec2_instance_role_assigned
    from .s3 import alarm_s3_bucket_policy_change, s3_lifecycle_policy_check
    from .lambda_fn import lambda_function_settings_check
    from .lb import alb_http_drop_invalid_header_enabled, alb_waf_enabled, elbv2_multiple_az, \
        elbv2_acm_certificate_required, clb_multiple_az
    from .auto_scaling import auto_scaling_multiple_az, auto_scaling_launch_config_requires_imdsv2, \
        auto_scaling_launch_config_hop_limit

    # refresh session
    def refresh_session(self):
        try:
            self.sts_client
        except AttributeError:
            logger.info('No need to refresh the session!')
            return
        remaining_duration_seconds = (
                self.creds['Credentials']['Expiration'] - datetime.datetime.now(pytz.utc)).total_seconds()

        if remaining_duration_seconds < 900:
            self.creds = self.sts_client.assume_role(
                RoleArn=self.iam_role_to_assume,
                RoleSessionName='RecommenderSession',
                DurationSeconds=3600
            )
            self.session = session.Session(
                aws_access_key_id=self.creds['Credentials']['AccessKeyId'],
                aws_secret_access_key=self.creds['Credentials']['SecretAccessKey'],
                aws_session_token=self.creds['Credentials']['SessionToken']
            )

    def get_compliance(self, regions=None) -> list:
        """
        :return:
        """
        if regions is None:
            regions = self.get_regions()

        compliance = []

        try:
            rds_clusters = self.list_rds_clusters(regions=regions)
        except ClientError as e:
            compliance.append(self.rds_cluster_iam_authentication_enabled(
                exception=True, exception_text=e.response['Error']['Code'])
            )
        else:
            compliance.append(self.rds_cluster_iam_authentication_enabled(cluster_list=rds_clusters))

        try:
            ec2_instances = self.list_ec2_instances(regions=regions)
        except ClientError as e:
            compliance.append(self.ec2_token_hop_limit_check(
                exception=True, exception_text=e.response['Error']['Code'])
            )
        else:
            compliance.append(self.ec2_token_hop_limit_check(ec2_instances=ec2_instances))
            compliance.append(self.ec2_instance_role_assigned(ec2_instances=ec2_instances))

        try:
            eni_lst = self.list_eni(regions=regions)
            sg_lst = self.list_security_groups(regions=regions)
        except ClientError as e:
            compliance.append(self.ec2_security_group_attached_to_eni(
                exception=True, exception_text=e.response['Error']['Code']))
        else:
            compliance.append(self.ec2_security_group_attached_to_eni(eni_lst=eni_lst, sg_lst=sg_lst))

        try:
            compliance.append(self.alarm_s3_bucket_policy_change(regions=regions))
        except ClientError as e:
            compliance.append(self.alarm_s3_bucket_policy_change(exception=True, exception_text=e.response['Error']['Code']))

        try:
            compliance.append(self.s3_lifecycle_policy_check())
        except ClientError as e:
            compliance.append(self.s3_lifecycle_policy_check(exception=True, exception_text=e.response['Error']['Code']))

        try:
            lambda_list = self.list_lambda_functions(regions=regions)
        except ClientError as e:
            compliance.append(self.lambda_function_settings_check(
                exception=True, exception_text=e.response['Error']['Code']
            ))
        else:
            compliance.append(self.lambda_function_settings_check(lambda_lst=lambda_list))

        try:
            elbv2_list = self.list_elbv2(regions=regions)
        except ClientError as e:
            compliance.append(self.alb_http_drop_invalid_header_enabled(exception=True, exception_text=e.response['Error']['Code']))
            compliance.append(self.alb_waf_enabled(exception=True, exception_text=e.response['Error']['Code']))
            compliance.append(self.elbv2_multiple_az(exception=True, exception_text=e.response['Error']['Code']))
            compliance.append(self.elbv2_acm_certificate_required(exception=True, exception_text=e.response['Error']['Code']))
        else:
            compliance.append(self.alb_http_drop_invalid_header_enabled(lb_list=elbv2_list))
            compliance.append(self.alb_waf_enabled(lb_list=elbv2_list))
            compliance.append(self.elbv2_multiple_az(lb_list=elbv2_list))
            compliance.append(self.elbv2_acm_certificate_required(lb_list=elbv2_list))

        try:
            asg_lst = self.list_auto_scaling_groups(regions=regions)
        except ClientError as e:
            compliance.append(self.auto_scaling_multiple_az(
                exception=True, exception_text=e.response['Error']['Code'])
            )
        else:
            compliance.append(self.auto_scaling_multiple_az(asg_lst=asg_lst))

        try:
            launch_configs = self.list_as_launch_configs(regions=regions)
        except ClientError as e:
            compliance.append(self.auto_scaling_launch_config_requires_imdsv2(
                exception=True, exception_text=e.response['Error']['Code'])
            )
            compliance.append(self.auto_scaling_launch_config_hop_limit(
                exception=True, exception_text=e.response['Error']['Code'])
            )
        else:
            compliance.append(self.auto_scaling_launch_config_requires_imdsv2(launch_config_list=launch_configs))
            compliance.append(self.auto_scaling_launch_config_hop_limit(launch_config_list=launch_configs))

        try:
            elb_list = self.list_elb(regions=regions)
        except ClientError as e:
            compliance.append(self.clb_multiple_az(
                    exception=True, exception_text=e.response['Error']['Code'])
                )
        else:
            compliance.append(self.clb_multiple_az(lb_list=elb_list))

        return compliance
