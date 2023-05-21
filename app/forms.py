from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField, FileField
from wtforms.validators import DataRequired, Length


class MovieForm(FlaskForm):
    title = StringField(
        'Название',
        validators=[DataRequired(message="Поле не должно быть пустым"),
                    Length(max=255, message='Введите заголовок длиной до 255 символов')]
    )
    
    description = TextAreaField(
        'Описание',
        validators=[DataRequired(message="Поле не должно быть пустым")]
    )
    
    image = FileField(
        'Изображение',
        validators=[DataRequired(message="Поле не должно быть пустым")]
    )
    
    submit = SubmitField('Добавить фильм')


class ReviewForm(FlaskForm):
    name = StringField(
        'Имя',
        validators=[DataRequired(message="Поле не должно быть пустым"),
                    Length(max=255, message='Введите заголовок длиной до 255 символов')]
    )
    
    text = TextAreaField(
        'Текст',
        validators=[DataRequired(message="Поле не должно быть пустым")]
    )
    
    rating = SelectField(
        'Оценка',
        choices=[(score, score) for score in range(1, 11)]
    )
    
    submit = SubmitField('Добавить отзыв')
