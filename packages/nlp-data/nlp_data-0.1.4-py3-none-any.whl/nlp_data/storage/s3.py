import boto3
from wasabi import msg
from rich.table import Table
from rich.console import Console
from typing import List, Optional
from pathlib import Path
import os
from zipfile import ZipFile
import tempfile


class S3Storage():
    def __init__(self, 
                 endpoint_url: str = "http://192.168.130.5:9005", 
                 access_key: str = "minioadmin", 
                 secret_key: str = "minioadmin"):
        super().__init__()
        self.s3 = boto3.resource(service_name='s3',
                                 endpoint_url=endpoint_url,
                                 aws_access_key_id=access_key,
                                 aws_secret_access_key=secret_key)
        self.s3_client = boto3.client('s3')
        
    @property
    def buckets(self):
        return [b.name for b in self.s3.buckets.all()]
    
    def get_bucket_files(self, bucket_name: str) -> List[str]:
        """获取某个bucket下的所有文件名称
        """
        return [obj.key for obj in self.s3.Bucket(bucket_name).objects.all()]
    
    def list_buckets(self):
        """基于rich库更好的展示所有的bucket的名称和文件数量"""
        table = Table(title="Buckets", show_header=True, header_style="bold magenta")
        table.add_column("Bucket Name", style="dim", width=12)
        table.add_column("File Count", justify="right", width=12)
        for bucket in self.s3.buckets.all():
            table.add_row(bucket.name, str(len(list(bucket.objects.all()))))
        console = Console()
        console.print(table)
        
    def list_files(self, bucket_name: str):
        """基于rich库更好的展示某个bucket下的所有文件的名称"""
        if bucket_name not in self.buckets:
            msg.fail(f"Bucket {bucket_name} does not exist.")
            return
        table = Table(title=f"Files in {bucket_name}", show_header=True, header_style="bold magenta")
        table.add_column("File Name", style="dim")
        for obj in self.s3.Bucket(bucket_name).objects.all():
            table.add_row(obj.key)
        console = Console()
        console.print(table)
        
    def create_bucket(self, bucket_name: str):
        """创建一个bucket
        """
        if bucket_name in self.buckets:
            msg.fail(f"Bucket {bucket_name} already exists.")
        else:
            self.s3.create_bucket(Bucket=bucket_name)
            msg.good(f"Bucket {bucket_name} created.")
            
    def delete_bucket(self, bucket_name: str):
        """删除一个bucket
        """
        if bucket_name not in self.buckets:
            msg.fail(f"Bucket {bucket_name} does not exist.")
        else:
            for obj in self.s3.Bucket(bucket_name).objects.all():
                obj.delete()
            self.s3.Bucket(bucket_name).delete()
            msg.good(f"Bucket {bucket_name} deleted.")
            
    def delete_file(self, bucket_name: str, file_name: str):
        """根据文件名删除文件
        """
        if bucket_name not in self.buckets:
            msg.fail(f'{bucket_name} not found')
        for obj in self.s3.Bucket(bucket_name).objects.all():
            if obj.key == file_name:
                obj.delete()
                msg.good(f'{file_name} deleted')
                return
            
    def upload_file(self, file_path: str, bucket_name: str, object_name: Optional[str] = None):
        """上传文件
        """
        file_path: Path = Path(file_path)
        if file_path.is_file():
            if bucket_name not in self.buckets:
                msg.fail(f'{bucket_name} not found')
            if object_name is None:
                object_name = file_path.name
            self.s3_client.upload_file(file_path, bucket_name, object_name)
            msg.good(f'{object_name} uploaded')
        else:
            msg.fail(f'{file_path} is not a file. if you want to upload a directory, use upload_dir')
            return
        
        
    def download_file(self, 
                      bucket_name: str, 
                      object_name: str, 
                      save_dir: Optional[str] = './',
                      decompress: bool = True):
        """下载文件
        """
        save_dir: Path = Path(save_dir)
        if not save_dir.is_dir():
            save_dir.mkdir(parents=True)
        if bucket_name not in self.buckets:
            msg.fail(f'{bucket_name} not found')
            return
        object_name = object_name.strip()
        all_files = self.get_bucket_files(bucket_name)
        if object_name not in all_files:
            msg.fail(f'{object_name} not found')
            return
        save_path = Path(save_dir, object_name)
        self.s3_client.download_file(bucket_name, object_name, save_path)
        if decompress:
            if object_name.endswith('.zip'):
                with ZipFile(save_path, 'r') as zip_file:
                    save_dir = Path(save_dir, object_name.split('.')[0])
                    zip_file.extractall(save_dir)
                # 删除压缩包
                save_path.unlink()
    
    
    def upload_dir(self, dir: str, bucket_name: str, object_name: Optional[str] = None):
        """zip压缩文件夹并上传
        """
        dir = Path(dir) 
        if dir.is_file():
            msg.fail(f'{dir} is not a directory')
            return
        if bucket_name not in self.buckets:
            msg.fail(f'{bucket_name} not found')
            return
        if object_name is None:
            temp_file = tempfile.tempdir + '/' + dir.name + '.zip'
            object_name = dir.name + '.zip'
        if object_name is not None:
            temp_file = tempfile.tempdir + '/' + object_name + '.zip'
        all_objects = self.get_bucket_files(bucket_name)
        if object_name in all_objects:
            msg.fail(f'{object_name} already exists')
            return
        with ZipFile(temp_file, 'w') as zip_file:
            zip_all_files(dir, zip_file, pre_dir='')
        self.upload_file(temp_file, bucket_name, object_name)
        zip_path = Path(temp_file)
        zip_path.unlink()
            
            
            
def zip_all_files(dir,zipFile,pre_dir):
    """递归压缩文件夹下的所有文件
    参数:
    - dir: 要压缩的文件夹路径
    - zipFile: zipfile对象
    - pre_dir: 压缩文件根目录
    """
    for f in os.listdir(dir):
        absFile=os.path.join(dir,f) #子文件的绝对路径
        pre_d = os.path.join(pre_dir,f)
        if os.path.isdir(absFile): #判断是文件夹，继续深度读取。
            zipFile.write(absFile, pre_d) #在zip文件中创建文件夹
            zip_all_files(absFile,zipFile, pre_dir=pre_d) #递归操作
        else: #判断是普通文件，直接写到zip文件中。
            zipFile.write(absFile, pre_d)