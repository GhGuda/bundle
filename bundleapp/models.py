from django.db import models
import secrets
from .paystack import PayStack

# Create your models here.
class Bundle(models.Model):
    amount = models.PositiveIntegerField()
    gig = models.TextField()
    ref = models.CharField(max_length=200)
    email = models.EmailField()
    number = models.TextField(null=True)
    verified = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    
    
    
    class Meta:
        ordering = ('-date',)
        
    def __str__(self):
        return f"Payment: {self.amount}"
    
    def save(self, *args, **kwargs) -> None:
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_ref = Bundle.objects.filter(ref=ref)
            
            if not object_with_similar_ref:
                self.ref = ref
        super().save(*args, **kwargs)
        
    def amount_value(self) -> int:
        # Just return the amount directly
        return self.amount
    
    def verify_payment(self):
        paystack = PayStack()
        status, result = paystack.verify_payment(self.ref, self.amount)
        if status:
            if result['amount'] == self.amount:
                self.verified = True
            
            self.save()
            if self.verified:
                return True
        return False
