class APIResponse:
    def __init__(self, status, data, message=None):
        self.status     =   status
        self.data       =   data
        self.message    =   message

    def respond(self):
        if self.message is None:
            return {
                "status"    :   self.status,
                "data"      :   self.data
            }
        else:
            return {
                "status"    :   self.status,
                "data"      :   self.data,
                "message"   :   self.message
            }