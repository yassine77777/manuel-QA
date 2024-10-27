from time import sleep,time

class TCa_01_Test_Authentification:
    REQ_ID = "Req-10"
    STATUS = "Ready"
    
    def prepare(self):
        self.start_Connexion()
		self.open_site("www.erp.com")
        self.create_account()
        
    def execute(self):
        self.enter_username("Mohamed")
        sleep(3)
        self.check_username_entred("Mohamed")
        self.enter_password("1234")
        sleep(3)
        self.check_password_entred("1234")
		self.clik_button("sign in")
		self.check_access_to_account()
        
    def clean_up(self):
		self.disonnect_from_account()
        self.close_site("www.erp.com")          
        self.clear_all_msg_senders() 
        