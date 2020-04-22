from django import forms
from product.models import Fruit , Option , Drink_info,Customer,Promotion
from django.contrib.auth.models import User
# Create the form class.

class UserForm(forms.ModelForm):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={ 'class' : 'form-control col-11',
                                        'placeholder' : 'username' }),
        
        label='Username : '
        )
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={ 'class' : 'form-control col-11',
                                        'placeholder' : 'ชื่อ' }),
        
        label='first name : '
        )
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={ 'class' : 'form-control  col-11',
                                        'placeholder' : 'นามสกุล' }),
        
        label='last name : '
        )
    email = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={ 'class' : 'form-control  col-11',
                                        'placeholder' : 'email' }),
        
        label='E-mail : '
        )
    password = forms.CharField(widget=forms.PasswordInput(attrs={ 'class' : 'form-control col-11',
                                        'placeholder' : 'รหัสผ่าน' }))
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
    class Meta():
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

class UserForm2(forms.ModelForm):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={ 'class' : 'form-control col-11',
                                        'placeholder' : 'username' }),
        
        label='Username : '
        )
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={ 'class' : 'form-control col-11',
                                        'placeholder' : 'ชื่อ' }),
        
        label='first name : '
        )
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={ 'class' : 'form-control  col-11',
                                        'placeholder' : 'นามสกุล' }),
        
        label='last name : '
        )
    email = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={ 'class' : 'form-control  col-11',
                                        'placeholder' : 'email' }),
        
        label='E-mail : '
        )
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
    class Meta():
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

class CustomerForm(forms.ModelForm):
    picture = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control-file col-5'}),required=False)
    address = forms.CharField(widget=forms.Textarea(attrs={ 'class' : 'form-control col-11'}))
    class Meta():
        model = Customer
        fields = ['address', 'picture']


class FruitForm(forms.ModelForm):
    picture = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control-file col-5'}),required=False)
    fruit_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={ 'class' : 'form-control col-5',
                                        'placeholder' : 'ชื่อของผลไม้' }),
        
        label='Fruit name:'
        )
    fruit_desc = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={ 'class' : 'form-control col-12', 
                                        'placeholder' : 'คำอธิบายของผลไม้'}),
        
        label='Fruit description:'
        )
    class Meta:
        model = Fruit
        fields = ('picture','fruit_name', 'fruit_desc')


class OptionForm(forms.ModelForm):
    picture = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control-file col-5'}),required=False)
    option_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={ 'class' : 'form-control col-5', 'placeholder' : 'ชื่อของ topping' }),
        label='Topping name:'
        )
    description = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={ 'class' : 'form-control col-12' , 'placeholder' : 'คำอธิบายของ topping' }),
        label='Topping description:'
        )
    price = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'type':'number', 'class' : 'form-control col-12' ,'placeholder' : 'ราคาของ topping'}),
        label='Topping price:')
    class Meta:
        model = Option
        fields = ('picture','option_name', 'description','price')

class DrinkForm(forms.ModelForm):
    picture = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control-file col-5'}),required=False)
    d_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={ 'class' : 'form-control col-5', 'placeholder' : 'ชื่อของเครื่องดื่ม' }),
        label='Drink name:'
        )
    d_desc = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={ 'class' : 'form-control col-12' , 'placeholder' : 'คำอธิบายเครื่องดื่ม' }),
        label='Drink description:'
        )
    how_to_make = forms.CharField(widget=forms.Textarea(attrs={ 'class' : 'form-control col-11'}),
     label='วิธีทำเครื่องดื่ม :')
    cost = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'type':'number', 'class' : 'form-control col-12' ,'placeholder' : 'ราคาของเครื่องดื่ม'}),
        label='Drinks price:')
    drink_type = forms.ChoiceField(choices=Drink_info.DRINK_TYPE, 
                    widget=forms.Select(attrs={'class' : 'form-control col-12'}))       
    class Meta:
        model = Drink_info
        fields = ('picture','d_name', 'd_desc', 'how_to_make', 'drink_type', 'cost') 

class PromotionForm(forms.ModelForm):
    name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={ 'class' : 'form-control col-5', 'placeholder' : 'ชื่อของ Promotion' }),
        label='Promotion name:'
        )
    s_date =  forms.DateField(widget=forms.DateInput(
        attrs={'type':'date', 'class' : 'form-control col-12' ,'placeholder' : 'วันที่เริ่ม promotion'}),
        label='Promotion start:'
    )
    e_date =  forms.DateField(widget=forms.DateInput(
        attrs= {'type':'date', 'class' : 'form-control col-12' ,'placeholder' : 'วันที่หมด promotion'})
        ,label='Promotion end:'
    )
    discount = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'type':'number', 'class' : 'form-control col-12' ,'placeholder' : 'ส่วนลดต่อเมนู(หน่วยเป็น บาท)'}),
        label='Discount : (หน่วยเป็น บาท)')
    promo_desc = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={ 'class' : 'form-control col-12' , 'placeholder' : 'คำอธิบาย Promotion' }),
        label='Promotion description:'
        )
    class Meta:
        model = Promotion
        fields = ('name','s_date','e_date','discount','promo_desc')