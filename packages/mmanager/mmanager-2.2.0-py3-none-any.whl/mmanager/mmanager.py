import os
import json
import requests
import traceback
from .dataresource import *
from .serverequest import *
from .log_keeper import *

class ModelManager:
    def  __init__(self, secret_key, base_url):
        self.base_url = base_url
        self.project_data = {}
        self.secret_key = secret_key
    
    def _get_headers(self, **kwargs):
        '''Returns headers for request
        '''
        headers = {'Authorization': 'secret-key {0}'.format(self.secret_key)}

        return headers

class Usecase(ModelManager):
  
    def post_usecase(self, usecase_info, forecasting_tables={}, forecasting_tables_fields={}, forecasting_feature_tabs={}):
        '''Post Usecase
        '''
        kwargs = {
            'headers': self._get_headers()
        }
       
        url = "%s/api/projects/" % self.base_url
        
        image_p = usecase_info.get('image', None)
        banner_p = usecase_info.get('banner', None)

        #for images
        files = {}
        if image_p:
            files.update({"image":open(image_p, 'rb')})

        if banner_p:
            files.update({"banner":open(banner_p, 'rb')})
        
        #for usecase_info
        data= {}
        files_key_list = ['image', 'banner']
        for key in files_key_list:
            usecase_info.pop(key, None)

        # Add all the usecase data into one
        data.update(usecase_info)

        # For Forecasting
        if usecase_info.get("usecase_type", None)=="Forecasting":
            data.update(forecasting_tables)
            data.update(forecasting_tables_fields)
            data.update(forecasting_feature_tabs)
    
        try:
            usecase = requests.post(url,
                    data=data, files=files, headers=kwargs['headers'])
            if usecase.status_code == 201:
                logger.info("Post usecase succeed with status code %s" % usecase.status_code)
            else:
                logger.error("Post usecase failed with status code %s" % usecase.status_code)
                if usecase.json()['name'][0]:
                    logger.error(usecase.json()['name'][0])
        except Exception as e:
            logger.error(str(e))
            usecase = e
            
        return usecase

    def patch_usecase(self, usecase_data, usecase_id):
        '''Update Usecase
        '''

        kwargs = {
            'headers': self._get_headers()
        }
       
        url = "%s/api/projects/%s/" % (self.base_url, usecase_id)

        #for images
        image_p = usecase_data.get('image', None)
        banner_p = usecase_data.get('banner', None)

        if image_p and banner_p:
            files={
                "image":open(image_p, 'rb'),
                "banner":open(banner_p, 'rb')
            }
        elif image_p:
            files={
                "image":open(image_p, 'rb'),
            }
        elif banner_p:
            files={
                "image":open(banner_p, 'rb'),
            }
        else:
            files = {}
        
        #for usecase_data
        data = usecase_data

        try:
            usecase = requests.patch(url,
                    data=data, files=files, headers=kwargs['headers'])
        except Exception as e:
            logger.error(str(e))
            usecase = e

        if usecase.status_code == 200:
            logger.info("Update usecase succeed with status code %s" % usecase.status_code)
        else:
            logger.error("Update usecase failed with status code %s" % usecase.status_code)
            if usecase.json()['name'][0]:
                logger.error(usecase.json()['name'][0])

        return usecase

    def delete_usecase(self, usecase_id):
        '''Delete Usecase
        '''

        kwargs = {
            'headers': self._get_headers()
        }
       
        url = "%s/api/projects/%s/" % (self.base_url, usecase_id)
        
        try:
            usecase = requests.delete(url, headers=kwargs['headers'])
        except Exception as e:
            logger.error(str(e))
            usecase = e

        if usecase.status_code == 204:
            logger.info("Delete usecase succeed with status code %s" % usecase.status_code)
        else:
            logger.info("Delete usecase failed with status code %s" % usecase.status_code)
            if usecase.json()['name'][0]:
                logger.error(usecase.json()['name'][0])
            
        return usecase

    def get_usecases(self):

        kwargs = {
            'headers': self._get_headers()
        }
        url = "%s/api/projects/get_usecases/" % self.base_url
        try:
            usecases = requests.get(url, headers=kwargs['headers'])
        except Exception as e:
            logger.error(str(e))
            usecases = e
        return usecases
    
    def get_detail(self, usecase_id):

        kwargs = {
            'headers': self._get_headers()
        }
        url = "%s/api/projects/%s/" % (self.base_url, usecase_id)
        try:
            usecases = requests.get(url, headers=kwargs['headers'])
        except Exception as e:
            logger.error(str(e))
            usecases = e

        return usecases

    def get_models(self, usecase_id):

        kwargs = {
            'headers': self._get_headers()
        }
        url = "%s/api/projects/getmodels/?usecase_id=%s" % (self.base_url, usecase_id)

        try:
            usecases = requests.get(url, headers=kwargs['headers'])
        except Exception as e:
            logger.error(str(e))
            usecases = e
        return usecases
    
    def load_cache(self, usecase_id):
        kwargs = {
            'headers': self._get_headers()
        }
        url = "%s/api/projects/data_loadcache/?usecase_id=%s" % (self.base_url, usecase_id)
        try:
            usecases = requests.get(url, headers=kwargs['headers'])
        except Exception as e:
            logger.error(str(e))
            usecases = e
        return usecases

class Applications(ModelManager):
    
    def post_application(self, data):
        kwargs = {
            'headers': self._get_headers()
        }
        url = "%s/api/applications/" % (self.base_url)

        try:
            application = requests.post(url,
                    data=data, headers=kwargs['headers'])
            
            if application.status_code == 201:
                logger.info("Post application succeed with status code %s" % application.status_code)
            else:
                logger.error("Post application failed with status code %s" % application.status_code)
                if application.json()['name'][0]:
                    logger.error(application.json()['name'][0])
        except Exception as e:
            logger.error(str(e))
            application = e

        return application
    
    def delete_application(self, usecase_id):
        '''Delete application
        '''

        kwargs = {
            'headers': self._get_headers()
        }
       
        url = "%s/api/applications/%s/" % (self.base_url, usecase_id)
        
        try:
            application = requests.delete(url, headers=kwargs['headers'])
        except Exception as e:
            logger.error(str(e))
            application = e

        if application.status_code == 204:
            logger.info("Delete application succeed with status code %s" % application.status_code)
        else:
            logger.info("Delete application failed with status code %s" % application.status_code)
            if application.json()['name'][0]:
                logger.error(application.json()['name'][0])
            
        return application
    
    def get_applications(self):
        kwargs = {
            'headers': self._get_headers()
        }
        url = "%s/api/applications/" % (self.base_url)

        try:
            applications = requests.get(url, headers=kwargs['headers'])
        except Exception as e:
            logger.error(str(e))
            applications = e
        return applications

class ExternalDatabase(ModelManager):
    def post_related_db(self, data):
        kwargs = {
            'headers': self._get_headers()
        }
        url = "%s/api/related_db/" % (self.base_url)

        try:
            related_db = requests.post(url,
                    data=data, headers=kwargs['headers'])
        except Exception as e:
            logger.error(str(e))
            related_db = e
        return related_db
    
    def get_related_db(self, data):
        kwargs = {
            'headers': self._get_headers()
        }
        url = "%s/api/related_db/" % (self.base_url)

        try:
            related_db = requests.get(url,
                    data=data, headers=kwargs['headers'])
        except Exception as e:
            logger.error(str(e))
            related_db = e
        return related_db

    def link_externaldb(self, data):
        kwargs = {
            'headers': self._get_headers()
        }
        url = "%s/api/externaldb_link/" % (self.base_url)

        try:
            db_link = requests.post(url,
                    data=data, headers=kwargs['headers'])
        except Exception as e:
            logger.error(str(e))
            db_link = e
        return db_link
    
    def get_externaldb_links(self):
        kwargs = {
            'headers': self._get_headers()
        }
        url = "%s/api/externaldb_link/" % (self.base_url)

        try:
            db_links = requests.get(url, headers=kwargs['headers'])
        except Exception as e:
            logger.error(str(e))
            db_links = e
        return db_links

class Model(ModelManager):

    def post_model(self, model_data, ml_options={}, create_sweetviz=True):
        '''Post Model
        '''
        url = "%s/api/models/" % self.base_url

        kwargs = {
            'headers': self._get_headers()
        }

        #for model_data
        model_data.update(ml_options)
        model_data.update({"create_sweetviz":create_sweetviz})
        data = get_model_data(model_data)

        #for model_files
        files = get_files(model_data)

        try:
            model = model_request(url, kwargs, data, ml_options, files)

            if model.status_code == 201:
                logger.info("Model creation succeed with status code %s" % model.status_code)
            else:
                logger.error("Model creation failed with status code %s" % (model.status_code))
                if model.json()['name'][0]:
                    logger.error(model.json()['name'][0])

        except Exception as e:
            logger.error(str(e))
            model = e
        
        return model
    
    def delete_model(self, model_id):

        '''Delete Model
        '''

        kwargs = {
            'headers': self._get_headers()
        }
        
        url = "%s/api/models/%s/" % (self.base_url, model_id)
        
        try:
            model = requests.delete(url, headers=kwargs['headers'])

            if model.status_code == 204:
                logger.info("Delete model succeed with status code %s" % model.status_code)
            else:
                logger.error("Delete model failed with status code %s" % model.status_code)
                if model.json()['name'][0]:
                    logger.error(model.json()['name'][0])

        except Exception as e:
            logger.error(str(e))
            model = e
            
        return model

    def patch_model(self, model_data, model_id, create_sweetviz=True):

        '''Update Model
        '''

        url = "%s/api/models/%s/" % (self.base_url, model_id)

        kwargs = {
            'headers': self._get_headers()
        }

        #for model_data
        data = model_data
        data.update({"create_sweetviz":create_sweetviz})      

        #for model_files
        files = get_files(model_data)

        try:
            model = requests.patch(url, data=data, files=files, headers=kwargs['headers'])

            if model.status_code == 200:
                logger.info("Update model succeed with status code %s" % model.status_code)
            else:
                logger.error("Update model failed with status code %s" % model.status_code)
                if model.json()['name'][0]:
                    logger.error(model.json()['name'][0])

        except Exception as e:
            logger.error(str(e))
            model = e

        return model

    def generate_report(self, model_id):
        '''Generate Model Report
        '''

        kwargs = {
            'headers': self._get_headers()
        }


        url = "%s/api/govrnreport/%s/generateReport/" % (self.base_url, model_id)

        try:
            model = requests.post(url, headers=kwargs['headers'])

            if model.status_code == 201:
                logger.info("Report Generation succeed with status code %s" % model.status_code)
            else:
                logger.error("Report Generation failed with status code %s" % model.status_code)
                if model.json()['name'][0]:
                    logger.error(model.json()['name'][0])

        except Exception as e:
            logger.error(str(e))
            model = e

        return model

    def get_details(self, model_id):
        kwargs = {
            'headers': self._get_headers()
        }
        url = "%s/api/models/%s/" % (self.base_url, model_id)
        try:
            model = requests.get(url, headers=kwargs['headers'])
        except Exception as e:
            logger.error(str(e))
            model = e

        return model
    
    def get_latest_metrics(self, model_id, metric_type):
        kwargs = {
            'headers': self._get_headers()
        }
        url = "%s/api/models/get_latest_metrics/?model_id=%s&&metric_type=%s" % (self.base_url, model_id, metric_type)
        try:
            model = requests.get(url, headers=kwargs['headers'])
        except Exception as e:
            logger.error(str(e))
            model = e

        return model

    def get_all_reports(self, model_id):
        kwargs = {
            'headers': self._get_headers()
        }
        url = "%s/api/models/get_all_reports/?model_id=%s" % (self.base_url, model_id)
        try:
            model = requests.get(url, headers=kwargs['headers'])
        except Exception as e:
            logger.error(str(e))
            model = e

        return model
