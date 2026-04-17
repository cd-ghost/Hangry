from django.db import models

class FoodItem(models.Model):
    """Food item model for the restaurant menu"""
    CATEGORY_CHOICES = [
        ('Italian', 'Italian'),
        ('Healthy', 'Healthy'),
        ('Desserts', 'Desserts'),
        ('Kids', 'Kids Menu'),
        ('Spicy', 'Spicy'),
    ]
    
    name = models.CharField(max_length=200, help_text="Food item name")
    description = models.CharField(max_length=500, help_text="Short description")
    price = models.DecimalField(max_digits=6, decimal_places=2, help_text="Price in rupees")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image_url = models.URLField(max_length=500, help_text="Image URL (from Unsplash, ImgBB, etc.)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['category', 'name']
        verbose_name_plural = "Food Items"
    
    def __str__(self):
        return f"{self.name} - ₹{self.price} ({self.category})"
