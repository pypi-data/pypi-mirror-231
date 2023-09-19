from bdaserviceutils import get_args, get_cmd_arg
from pysparkutilities.spark_initializer import spark_initializer
from pysparkutilities import ds_initializer
from .generic_service import GenericService
from alidaargparser import get_asset_property


class SparkService(GenericService):
    def __init__(self, parser, additional_config=[]):
        super().__init__(parser)
        self._args = get_args()
        print(self._args)

        #additional_config = additional_config.append(('spark.jars.packages', 'io.prestosql:presto-jdbc:350'))
        self.spark = spark_initializer("Test-model", self._args, additional_config=additional_config)

    def get_dataset(self, name="input_dataset"):
        data = ds_initializer.load_dataset(sc=self.spark, name=name, read_all=False)
        return data

    def save_dataset(self, dataset, name="output_dataset"):
        ds_initializer.save_dataset(sc=self.spark,name=name, df=dataset)#, output_dest=self._args['output-dataset'])

    def download_model(self, name='input_model'):
        
        storage_type = get_asset_property(asset_name=name, property='storage_type')

        if storage_type == "hdfs":
            return get_cmd_arg('hdfsUrl') + get_asset_property(asset_name=name)
        
        elif storage_type == "minio":
            return "s3a://" + get_asset_property(asset_name=name, property='minio_bucket')+ "/" + get_asset_property(asset_name=name)
        
        return get_asset_property(asset_name=name)

    def upload_model(self, model, name='output_model'):
        if isinstance(model, str):
            super().upload_model(model, name)
        else:
            storage_type = get_asset_property(asset_name=name, property='storage_type')
            if storage_type == "hdfs":
                model_path = get_cmd_arg('hdfsUrl') + get_asset_property(asset_name=name)
            
            elif storage_type == "minio":
                model_path = "s3a://" + get_asset_property(asset_name=name, property='minio_bucket')+ "/" + get_asset_property(asset_name=name)
            
            model.write().overwrite().save(model_path)