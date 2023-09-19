#************************************************************************
# Copyright 2021 O7 Conseils inc (Philippe Gosselin)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#************************************************************************
"""Module allows to view and access EC2 Instances"""


#--------------------------------
#
#--------------------------------
import pprint
import logging
import subprocess

from o7util.table import TableParam, ColumnParam, Table
import o7util.menu as o7m
import o7util.input as o7i
import o7util.terminal as o7t

import o7lib.aws.base


logger=logging.getLogger(__name__)

#*************************************************
#
#*************************************************
class Ec2(o7lib.aws.base.Base):
    """Class for EC2 for a Profile & Region"""

    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html

    #*************************************************
    #
    #*************************************************
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ec2 = self.session.client('ec2')

        self.instances = []

        self.instance = {}
        self.instance_status = {}


    #*************************************************
    #
    #*************************************************
    def load_instances(self):
        """Load all instances in Region"""

        logger.info('load_instances')

        # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_instances.html
        paginator = self.ec2.get_paginator('describe_instances')
        self.instances = []
        param={}

        for page in paginator.paginate(**param):
            for reservation in page['Reservations'] :
                self.instances.extend(reservation.get('Instances', []))

        # Reformat some data
        for instance in self.instances:

            instance['StateName'] = instance['State'].get('Name', 'na')

            for tag in instance.get('Tags',[]):
                if tag['Key'] == 'Name':
                    instance['Name'] = tag['Value']
                    break

        logger.info(f'LoadInstances: Number of Instances found {len(self.instances)}')

        return self

    #*************************************************
    #
    #*************************************************
    def load_instance(self, instance_id : str):
        """Load a specific instance"""

        logger.info(f'load_instance: {instance_id}')

        responce  = self.ec2.describe_instances(InstanceIds=[instance_id])
        self.instance = responce['Reservations'][0]['Instances'][0]

        responce  = self.ec2.describe_instance_status(InstanceIds=[instance_id])

        self.instance_status = responce['InstanceStatuses'][0] if len(responce['InstanceStatuses']) > 0 else {}


        return self


    #*************************************************
    #
    #*************************************************
    def start_instance(self):
        """Start an instance"""

        instance_id = self.instance.get("InstanceId", 'na')
        logger.info(f'start_instance instance_id={instance_id}')

        answer = o7i.is_it_ok(f'Confirm you want to START instance {instance_id}')
        if answer is False:
            return

        # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/start_instances.html
        response = self.ec2.start_instances(InstanceIds=[instance_id])
        pprint.pprint(response)

    #*************************************************
    #
    #*************************************************
    def stop_instance(self):
        """Stop an instance"""

        instance_id = self.instance.get("InstanceId", 'na')
        logger.info(f'stop_instance instance_id={instance_id}')

        answer = o7i.is_it_ok(f'Confirm you want to STOP instance {instance_id}')
        if answer is False:
            return

        # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/start_instances.html
        response = self.ec2.stop_instances(InstanceIds=[instance_id])
        pprint.pprint(response)

    #*************************************************
    #
    #*************************************************
    def terminate_instance(self):
        """Terminate an instance"""

        instance_id = self.instance.get("InstanceId", 'na')
        logger.info(f'terminate_instance instance_id={instance_id}')

        answer = o7i.is_it_ok(f'Confirm you want to TERMINATE instance {instance_id}')
        if answer is False:
            return

        # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/terminate_instances.html
        response = self.ec2.terminate_instances(InstanceIds=[instance_id])
        pprint.pprint(response)

    #*************************************************
    #
    #*************************************************
    def display_instance(self):
        """Display Instances"""

        self.load_instance(self.instance.get("InstanceId", 'na'))

        print('')

        print(f'Instance Id: {self.instance.get("InstanceId", "")}')
        print(f'Type: {self.instance.get("InstanceType", "")}')
        print(f'Launch: {self.instance.get("LaunchTime", "")}')
        print(f'Private IP: {self.instance.get("PrivateIpAddress", "")}')
        print(f'Public IP: {self.instance.get("PublicIpAddress", "")}')

        print()
        print(f'State: {o7t.format_aws_state(self.instance["State"]["Name"])}')
        print(f'State Reason: {self.instance.get("StateReason", "-")}')
        print(f'Instance Status: {self.instance_status.get("InstanceStatus",{}).get("Status","na")}')
        print(f'System Status: {self.instance_status.get("SystemStatus",{}).get("Status","na")}')
        print()

        Table(
            TableParam(
                title='Tags',
                columns = [
                    ColumnParam(title = 'Key',  type = 'str',   data_col = 'Key'  ),
                    ColumnParam(title = 'Value',type = 'str',   data_col = 'Value'),
                ]
            ),
            self.instance.get("Tags", [])
        ).print()
        print()




    #*************************************************
    #
    #*************************************************
    def display_instances(self):
        """Display Instances"""

        self.load_instances()

        params = TableParam(
            columns = [
                ColumnParam(title = 'id',          type = 'i',    min_width = 4  ),
                ColumnParam(title = 'Name',     type = 'str',  data_col = 'Name'),
                ColumnParam(title = 'Instance Id', type = 'str',  data_col = 'InstanceId'),
                ColumnParam(title = 'Type',        type = 'str', data_col = 'InstanceType'),
                ColumnParam(title = 'Launch' ,     type = 'date',  data_col = 'LaunchTime'),
                ColumnParam(title = 'KeyName',     type = 'str',  data_col = 'KeyName'),
                ColumnParam(title = 'Private IP',     type = 'str',  data_col = 'PrivateIpAddress'),
                ColumnParam(title = 'Public IP',     type = 'str',  data_col = 'PublicIpAddress'),

                ColumnParam(title = 'State'  ,     type = 'str',  data_col = 'StateName', format = 'aws-state'),
                ColumnParam(title = 'Reason'  ,     type = 'str',  data_col = 'StateReason')
            ]
        )
        print()
        Table(params, self.instances).print()
        print('Help: aws ssm start-session --target <instanceId>')

        return self




    #*************************************************
    #
    #*************************************************
    def start_session_shell(self):
        """Start a shell session on the instance"""

        instance_id = self.instance.get("InstanceId", 'na')
        aws_cred = self.session.get_credentials()

        cmd = f'AWS_ACCESS_KEY_ID={aws_cred.access_key} && \n'
        cmd += f'AWS_SECRET_ACCESS_KEY={aws_cred.secret_key} && \n'
        cmd += f'aws --region {self.session.region_name} ssm start-session --target {instance_id}'
        print(f'Command: {cmd}')
        subprocess.call(cmd, shell = True)

    #*************************************************
    #
    #*************************************************
    def start_forward_rdp(self):
        """Start port forwarding for RDP"""

        instance_id = self.instance.get("InstanceId", 'na')
        aws_cred = self.session.get_credentials()

        cmd = f'AWS_ACCESS_KEY_ID={aws_cred.access_key} && \n'
        cmd += f'AWS_SECRET_ACCESS_KEY={aws_cred.secret_key} && \n'
        cmd += f'aws --region {self.session.region_name} ssm start-session --target {instance_id}'
        cmd += ' --document-name AWS-StartPortForwardingSession --parameters "localPortNumber=54321,portNumber=3389"'
        print(f'Command: {cmd}')
        print('Connect local RDP to localhost:54321')
        subprocess.call(cmd, shell = True)

    #*************************************************
    #
    #*************************************************
    def start_forward_port(self):
        """Start post forwarding session"""

        instance_id = self.instance.get("InstanceId", 'na')
        aws_cred = self.session.get_credentials()

        remote_host = o7i.input_string('Enter Remote Host (where to forward):')
        remote_port = o7i.input_int('Enter Remote Port (where to forward):')
        local_port = o7i.input_int('Enter Local Port (on this machine):')

        cmd = f'AWS_ACCESS_KEY_ID={aws_cred.access_key} && \n'
        cmd += f'AWS_SECRET_ACCESS_KEY={aws_cred.secret_key} && \n'
        cmd += f'aws --region {self.session.region_name} ssm start-session --target {instance_id} '
        cmd += '--document-name AWS-StartPortForwardingSessionToRemoteHost  '
        cmd += f'--parameters host="{remote_host}",localPortNumber={local_port},portNumber={remote_port}'
        print(f'Command: {cmd}')
        print(f'Connect to localhost:{local_port}')
        subprocess.call(cmd, shell = True)

    #*************************************************
    #
    #*************************************************
    def menu_instance(self, index):
        """Instances view & edit menu"""

        if  not 0 < index <= len(self.instances):
            return self

        self.instance = self.instances[index - 1]

        obj = o7m.Menu(
            exit_option = 'b',
            title=f'EC2 Instance - {self.instance.get("InstanceId","na")}',
            title_extra=self.session_info(), compact=False
        )
        obj.add_option(o7m.Option(key='r',      name='Display Raw Data',callback=lambda: pprint.pprint(self.instance)))
        obj.add_option(o7m.Option(key='s',      name='Display Raw Status',callback=lambda: pprint.pprint(self.instance_status)))
        obj.add_option(o7m.Option(key='start',  name='Start Instance', callback=self.start_instance ))
        obj.add_option(o7m.Option(key='stop',  name='Stop Instance', callback=self.stop_instance ))
        obj.add_option(o7m.Option(key='terminate',  name='Terminate Instance', callback=self.terminate_instance ))
        obj.add_option(o7m.Option(key='shell',  name='Open Shell Session',callback=self.start_session_shell))
        obj.add_option(o7m.Option(key='rdp',    name='RDP Forwarding',callback=self.start_forward_rdp))
        obj.add_option(o7m.Option(key='pf',     name='Port Forwarding',callback=self.start_forward_port))

        obj.display_callback = self.display_instance
        obj.loop()



    #*************************************************
    #
    #*************************************************
    def menu_instances(self):
        """Instances view & edit menu"""

        obj = o7m.Menu(exit_option = 'b', title='EC2 Instances', title_extra=self.session_info(), compact=True)

        obj.add_option(o7m.Option(
            key='r',
            name='Display Raw Data',
            short='Raw',
            callback=lambda: pprint.pprint(self.instances)
        ))
        obj.add_option(o7m.Option(
            key='int',
            name='Details for an Instance',
            short='Details',
            callback=self.menu_instance
        ))


        obj.display_callback = self.display_instances
        obj.loop()

        return self




#*************************************************
#
#*************************************************
def menu(**kwargs):
    """Run Main Menu"""
    Ec2(**kwargs).menu_instances()



#*************************************************
#
#*************************************************
if __name__ == "__main__":

    logging.basicConfig(
        level=logging.INFO,
        format="[%(levelname)-5.5s] [%(name)s] %(message)s"
    )

    ec2_obj = Ec2().menu_instances()
    # ec2_obj = Ec2().load_instance('i-01ba040ef1b4671da')
    # pprint.pprint(ec2_obj.instance_status)
    # Ec2().MenuInstances()
