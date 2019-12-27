from django import forms
from django.contrib import admin

from .models import Sudoku


class SudokuForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk is not None:
            size = self.instance.box_length * self.instance.box_width
            self.fields["puzzle"].widget.attrs.update({"cols": size, "rows": size})

    class Meta:
        model = Sudoku
        fields = forms.ALL_FIELDS
        widgets = {
            "puzzle": forms.Textarea(attrs={"cols": 9, "rows": 9}),
        }


@admin.register(Sudoku)
class SudokuAdmin(admin.ModelAdmin):
    form = SudokuForm
    list_display = ("id", "rank", "box_width", "box_length", "is_daily", "created_at")
    list_filter = ("is_daily",)
