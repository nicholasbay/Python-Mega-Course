import detector
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool

def main():
    df = detector.motion_detector()

    # Creating figure object
    fg = figure(x_axis_type='datetime', height=200, width=1000, title="Motion Graph")

    # Modifying figure object
    fg.yaxis.minor_tick_line_color = None
    fg.ygrid.grid_line_color = None

    # Creating hover object
    hover = HoverTool(tooltips=[('Enter Time','@Enter Time'), ('Exit Time','@Exit Time')])

    # Preparing data
    fg.quad(left=df['Enter Time'], right=df['Exit Time'], top=1, bottom=0, color='green')

    # Preparing output file
    output_file('Section 18 - Motion Detector App/motion_graph.html')

    print("Motion graph saved successfully.")


if __name__ == '__main__':
    main()