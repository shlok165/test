from django.db import models

class ServiceRequest(models.Model):
    PRIORITY_CHOICES = [
        ('normal', 'Normal'),
        ('urgent', 'Urgent'),
        ('emergency', 'Emergency'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    preferred_contact = models.CharField(max_length=10)
    service_type = models.CharField(max_length=50)
    urgency = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    message = models.TextField()
    attachment = models.FileField(upload_to='service_requests/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'home'

    def __str__(self):
        return f"{self.name} - {self.service_type}"
