# TODO: This is an example file which you should delete after implementing
from dotenv import load_dotenv
import json
from circles_local_database_python.connector import Connector
from logger_local.Logger import Logger
from logger_local.LoggerComponentEnum import LoggerComponentEnum
from circles_local_database_python.connector import Connector
from circles_local_database_python.generic_crud import GenericCRUD
load_dotenv()

# Setup the logger: change YOUR_REPOSITORY variable name and value
YOUR_REPOSITORY_COMPONENT_ID = 212  # ask your team leader for this integer
YOUR_REPOSITORY_COMPONENT_NAME = "api-management-local-python-package"
DEVELOPER_EMAIL = "heba.a@circ.zone"
object1 = {
    'component_id': YOUR_REPOSITORY_COMPONENT_ID,
    'component_name': YOUR_REPOSITORY_COMPONENT_NAME,
    'component_category': LoggerComponentEnum.ComponentCategory.Code.value,
    'developer_email': DEVELOPER_EMAIL
}
logger=Logger.create_logger(object=object1)
class ExampleClass(GenericCRUD):
    def __init__(self) -> None:
        pass

    @staticmethod
    def insert_data_into_table(table_name, data):
        try:
            # Create a Python dictionary
            json_data = {
                'api_type_id': data[0],  # Replace with the actual column name
                'endpoint': data[1],  # Replace with the actual column name
                'outgoing_header': data[2],  # Replace with the actual column name
                'outgoing_body': data[3],  # Replace with the actual column name
                 'outgoing_body_signigicant_fields_hash': data[4],  # Replace with the actual column name
                'incoming_message': data[5]  # Replace with the actual column name
            }

            # Create the GenericCRUD instance and insert data
            crud_instance = GenericCRUD(schema_name='api_call')
            crud_instance.insert(table_name=table_name, json_data=json_data)
        except Exception as e:
            print(f"Error inserting data: {str(e)}")

