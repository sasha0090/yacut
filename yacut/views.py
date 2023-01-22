from flask import flash, render_template, Markup, redirect, url_for, abort

from yacut.forms import CutForm
from . import app
from .models import URLMap
from .utils import create_url_map


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = CutForm()
    if form.validate_on_submit():
        custom_id = form.custom_id.data
        original_link = form.original_link.data

        if custom_id and URLMap.query.filter_by(short=custom_id).first():
            flash(f'Имя {custom_id} уже занято!')
            return render_template('cut_url.html', form=form)

        url_map = create_url_map(original_link, custom_id)

        short_link = url_for(
            'short_url_view',
            custom_id=url_map.short,
            _external=True
        )

        flash_url = f'<br><a href="{short_link}">{short_link}</a>'
        flash(Markup(f'Ваша ссылка готова:{flash_url}'))
    return render_template('cut_url.html', form=form)


@app.route('/<string:custom_id>')
def short_url_view(custom_id):
    url = URLMap.query.filter_by(short=custom_id).first()
    if not url:
        abort(404)
    return redirect(url.original)

