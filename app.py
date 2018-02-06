#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, request
import logging
from logging import Formatter, FileHandler

from get_tweets import get_tweets
from toxicity import *

#from bokeh.io import show, output_file
#from bokeh.plotting import figure
#from bokeh.embed import components

def at_remover(s):
    if s[0]=='@':
        s = s[1:]
    return s

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#


@app.route('/')
def home():
    return render_template('pages/input.html')

@app.route('/output')
def output():
    screen_name = str(request.args.get('entity'))
    if screen_name == '':
        screen_name = 'RealDonaldTrump'
    screen_name = at_remover(screen_name)

    twitter_account = get_tweets(screen_name, 500)

    if twitter_account.shape[0]==0:
		return render_template("pages/uncertain.html")

    else:
        df, notable = toxicity(twitter_account)

        #x = list(df.columns.values)
        #plot = figure(x_range=x, plot_height=350,
               #toolbar_location=None, tools="")

        #plot.vbar(x=x, top=list(df.loc['mean'].values), width=0.9, legend="Mean")
        #plot.vbar(x=x, top=list(df.loc['max'].values), width=0.9, legend="Maximum", alpha = 0.5)

        #plot.xgrid.grid_line_color = None
        #plot.y_range.start = 0
        #plot.y_range.end = 1

        #script, div = components(plot)

        if len(notable)==0:
            notable = [{'category': 'Not Toxic', 'text': 'no bad tweets found for this account!'}]

        return render_template('pages/output.html',\
                        screen_name=screen_name, worst_tweet=notable)#, the_div=div, the_script=script)

@app.route('/about')
def about():
    return render_template('pages/about.html')

#----------------------------------------------------------------------------#
# Error handlers.
#----------------------------------------------------------------------------#

@app.errorhandler(500)
def internal_error(error):
    #db_session.rollback()
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.debug = True
    app.run()


# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
