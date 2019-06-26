#encoding:utf-8

class FormMixin(object):
    def get_errors(self):
        if hasattr(self,'errors'):
            errors = self.errors.get_json_data()
            #{"telephone":['','']}
            new_errors = {}
            for key,message_dicts in errors.items():

                for message_dict in  message_dicts:
                    messages = []
                    for message in message_dict:
                        messages.append(message['message'])
                    new_errors[key] = messages
            return new_errors
        else:
            return {}

