import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'asdkjas3njadnj23nrn2mlsadasda'