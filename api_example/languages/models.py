from django.db import models

class Paradigm(models.Model):
    name = models.CharField(max_length=50)                              #Primary_Key

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=50)
    paradigm = models.ForeignKey(Paradigm, on_delete=models.CASCADE)    #Foreign_Key
    
    def __str__(self):
        return self.name

class Programmer(models.Model):
    name = models.CharField(max_length=50)
    languages = models.ManyToManyField(Language)                        #ManyToMany
                                                                        #OneToOne
                                                                        #OneToMany
                                                                        #ManyToOne 
                                                                        
    def __str__(self):
        return self.name
