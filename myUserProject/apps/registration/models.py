from __future__ import unicode_literals
import bcrypt,re
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
from django.db import models

# Create your models here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') #email validation string
NAME_REGEX = re.compile(r'^[a-zA-Z ]+$') #first name/last name validation string
U_NAME_REGEX = re.compile(r'^[a-zA-Z0-9]+$') #first name/last name validation string
now = (datetime.now().strftime('%Y-%m-%d'))

class UserManager(models.Manager):
    def register_validator(self, postdata):
        errors = {}
        err = False        
                 
        if len(postdata['email']) < 3 or (not EMAIL_REGEX.match(postdata['email'])):
            errors["email"] = "Email is INVALID, Try again"
            err = True
        zcount = User.objects.filter(email = postdata['email'] ).count()
        print(" email exists/count:",zcount)
        if zcount > 0:
            errors["email"] = "That email is in use, Try Logging in"
            return [False,errors]  
        print( 'name: ',postdata['name'])
        if len(postdata['name']) < 3 or (not NAME_REGEX.match(postdata['name'])) :
            errors["name"] = "Name must be letters and more than 3 characters"        
            err = True 
        if len(postdata['alias']) < 3 or (not NAME_REGEX.match(postdata['alias'])) :
            errors["alias"] = "Alias must be letters and more than 3 characters"        
            err = True
        if len(postdata['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"
            err - True
        if (postdata['password']) != postdata['confirm'] or postdata['confirm'] == "" :
            errors["confirm"] = "Password and Confirm must match"
            err = True
        print( 'Birthday? :',now,' bday:',postdata['birthdate'])
        if (postdata['birthdate'])  == '' or (postdata['birthdate'] >= now )  :
            errors["birthdate"] = "Invalid Birth date entered"
            err = True
        if err:    
            return [False,errors]

        #hash1 = bcrypt.hashpw(postdata['password'].encode(), bcrypt.gensalt()) #bcrypt'd Password
        saltp = bcrypt.gensalt(14)
        hash1 = bcrypt.hashpw(postdata['password'].encode("utf-8"),saltp)
        # User.password = hash1        
        # test, create will save automatically..
        
        new = User.objects.create(name = postdata['name'], birthdate = postdata['birthdate'], \
        alias=postdata['alias'], email=postdata['email'],password=hash1.decode() )
        
        # user = User.objects.get(email=postdata['email'])
        user = User.objects.get(email=postdata['email']).id
        return [True,user]


    def login_validator(self, postData): # Validate Login Data
        errors = {}

        err = False
        if len(postData['email']) == 0:
            errors["email"] = " The Email ID cannot be blank"
            err = True
        if len(postData['password']) == 0:
            errors["password"] = " The Password cannot be blank"
            err = True
        if User.objects.filter(email=postData['email']).count() == 0 :        
            errors["email"] = " That Email ID is not listed, try again or Register"
            err = True
        if err:
            return [False,errors]
        else: # Verify Password
            hash1 = User.objects.get(email=postData['email']).password
            if bcrypt.checkpw(postData['password'].encode(), hash1.encode()):
                user = User.objects.get(email=postData['email']).id
                alias = User.objects.get(email=postData['email']).alias
                print("user email : ",postData['email'],"  alias : ",alias)
                return [True,user] 
            else:
                errors["password"] = " That Password is InValid"
                return [False,errors]
            
    def update_validator(self, postdata):
        errors = {}
        err = False   
        if len(postdata['email']) < 3 or (not EMAIL_REGEX.match(postdata['email'])):
            errors["email"] = "Email is INVALID, Try again"
            err = True

        # zcount = User.objects.filter(email = postdata['email'] ).count()
        # print(" email exists/count:",zcount)
        # if zcount > 0:
        #     errors["email"] = "That email is in use, Try Logging in"
        #     return [False,errors]  
        
        print( 'name: ',postdata['name'])
        if len(postdata['name']) < 3 or (not NAME_REGEX.match(postdata['name'])) :
            errors["name"] = "Name must be letters and more than 3 characters"        
            err = True 
        if len(postdata['alias']) < 3 or (not NAME_REGEX.match(postdata['alias'])) :
            errors["alias"] = "Alias must be letters and more than 3 characters"        
            err = True

        # if len(postdata['password']) < 8:
        #     errors["password"] = "Password should be at least 8 characters"
        #     err - True
        # if (postdata['password']) != postdata['confirm'] or postdata['confirm'] == "" :
        #     errors["confirm"] = "Password and Confirm must match"
        #     err = True

        print( 'Birthday? :',now,' bday:',postdata['birthdate'])
        if (postdata['birthdate'])  == '' or (postdata['birthdate'] >= now )  :
            errors["birthdate"] = "Invalid Birth date entered"
            err = True
        if err:    
            return [False,errors]
        else:   # Valid- save
           U = User.objects.get(id= postdata['user_id'])
           U.name = postdata['name']
           U.alias = postdata['alias']
           U.email = postdata['email']           
           U.birthdate = postdata['birthdate']
           U.firstname = postdata['firstname']
           U.middlename = postdata['middlename']
           U.lastname = postdata['lastname']
           #U.my_hello = postdata['my_hello']
           U.address = postdata['address']
           U.address2 = postdata['address2']
           U.city = postdata['city']
           U.state = postdata['state']
           U.zip = postdata['zip']
           U.phone = postdata['phone']
           U.cell = postdata['cell']
          
           U.save()
           return [True]
        

            

class User(models.Model):
    # name = models.CharField(max_length=255)
    # alias = models.CharField(max_length=255)
    # email = models.CharField(max_length=255)    # ? unique=True
    # birthdate = models.DateField()   # DateTimeField
    # password = models.CharField(max_length=255)

    #email2 = models.EmailField(max_length=75) # 254 default
    
    name = models.CharField(max_length=50)
    alias = models.CharField(max_length=50)         # SlugField()   Az99_-
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=75)         # models.EmailField(max_length=75) # 254 default
    birthdate = models.DateField()   

    firstname = models.CharField(max_length=50, blank=True)
    middlename = models.CharField(max_length=50, blank=True)
    lastname = models.CharField(max_length=50, blank=True)
    my_hello = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=128, blank=True)
    address2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=128, blank=True)
    state = models.CharField(max_length=128, blank=True)
    zip = models.CharField(max_length=128, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    cell = models.CharField(max_length=15, blank=True)
    location = models.CharField(max_length=128, blank=True)
    # friends = models.ManyToManyField('self',related_name='friends_with')

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
     # *************************
    # Connect an instance of BlogManager to our Blog model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    objects = UserManager()
    # *************************
    def __repr__(self):
        return "<user: {} {} {} {} {}>".format(self.name, self.alias, self.email, self.birthdate, self.pk)
    

