import os
import pandas as pd
import uuid
 
 
class FileSettings(object):
    def __init__(self, arquivo, linhas=100):
        self.arquivo = arquivo
        self.linhas = linhas
 
 
class FileSplitter(object):
 
    def __init__(self, file_settings):
        self.file_settings = file_settings
 
        if type(self.file_settings).__name__ != "FileSettings":
            raise Exception("Please pass correct instance ")
 
        self.df = pd.read_csv(self.file_settings.arquivo,
                              chunksize=self.file_settings.linhas)
 
    def run(self, directory="temp"):
 
        try:os.makedirs(directory)
        except Exception as e:pass
 
        counter = 0
 
        while True:
            try:
                arquivo = "{}/{}_{}_row_{}_{}.csv".format(
                    directory,  self.file_settings.arquivo.split(".")[0], counter, self.file_settings.linhas, uuid.uuid4().__str__()
                )
                df = next(self.df).to_csv(arquivo)
                counter = counter + 1
            except StopIteration:
                break
            except Exception as e:
                print("Error:",e)
                break
 
        return True
 
 
def main():
    helper =  FileSplitter(FileSettings(
        arquivo ='teste_split.csv',
        linhas=1000
    ))
    helper.run()
 
main()