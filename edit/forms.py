from django import forms
# from edit.models import ShopInfo
from kakao.models import Geocafe

class ShopForm(forms.ModelForm):
    class Meta:
        model = Geocafe
        fields = ['post_code', 'name', 'addr', 'type', 'open', 'tel', 'x', 'y']
        widgets = {
            'post_code': forms.HiddenInput(),
            'name': forms.TextInput(attrs={'id': 'name',
                                           'class': 'form-control'}),
            'addr': forms.TextInput(attrs={'id': 'addr',
                                           'class': 'form-control'}),
            'type': forms.TextInput(attrs={'id': 'type',
                                           'class': 'form-control'}),
            'open': forms.TextInput(attrs={'id': 'open',
                                           'class': 'form-control'}),
            'tel': forms.TextInput(attrs={'id': 'p_title',
                                          'class': 'form-control'}),
            'x': forms.HiddenInput(),
            'y': forms.HiddenInput(),
        }

        labels = {
            'post_code': '수정하지마세요',
            'name': '매장명',
            'addr': '매장주소',
            'type': '업종',
            'open': '영업여부  ex)영업/정상 or 폐업 ',
            'tel': '매장전화번호',
            'x': '수정하지마세요',
            'y': '수정하지마세요',
        }

    def __init__(self, *args, **kwargs):
        super(ShopForm, self).__init__(*args, **kwargs)
        # self.fields['name'].widget.attrs['maxlength'] = 100
        self.fields['post_code'].required = False
        self.fields['x'].required = False
        self.fields['y'].required = False

    # def __str__(self):
    #     return self.post_code, self.x, self,y

