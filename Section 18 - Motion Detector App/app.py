# Motion Detector App
# Functionalities:
# 1. Detects object motion through webcam feed
# 2. Time that object enters & exits frame is recorded and saved into 'motion_records.csv'
# 3. Enter & exit times plotted on a graph for easy visualisation

import cv2, time, pandas
from datetime import datetime
from bokeh.plotting import figure, output_file, save
from bokeh.models import HoverTool, ColumnDataSource

def main():
    motion_data = detector()
    plotter(motion_data)


def detector():
    # Reference frame of the background
    first_frame = None
    # Boolean list of motion detected
    motion_list = [None, None]
    # Lists of enter & exit times
    enter_times = []
    exit_times = []

    video = cv2.VideoCapture(0)
    # Delay to ensure webcam feed has been loaded, otherwise first_frame is all black
    time.sleep(0.1)

    while True:
        check, frame = video.read()

        motion = False

        grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        grey_frame = cv2.GaussianBlur(grey_frame, (25,25), 0)

        if first_frame is None:
            first_frame = grey_frame
            continue

        delta_frame = cv2.absdiff(first_frame, grey_frame)

        thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
        # Remove small black gaps from white areas in the threshold frame
        thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

        # Extract all contours from threshold frame
        (contours, _) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        for contour in contours:
            # Ignore smaller contours
            if cv2.contourArea(contour) < 40000:
                continue

            motion = True
            
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

        motion_list.append(motion)
        motion_list = motion_list[-2:]

        # Object entered frame (no motion -> motion)
        if motion_list[-2] is False and motion_list[-1] is True:
            enter_times.append(datetime.now())
        # Object exited frame (motion -> no motion)
        elif motion_list[-2] is True and motion_list[-1] is False:
            exit_times.append(datetime.now())

        cv2.imshow('Video Feed', frame)

        # Exit loop on 'q' keypress
        if cv2.waitKey(1) & 0xFF == ord('q'):
            if motion is True:
                exit_times.append(datetime.now())
            break

    video.release()
    cv2.destroyAllWindows()

    times = {'Enter Time': enter_times, 'Exit Time': exit_times}
    df = pandas.DataFrame(times)

    # Save DataFrame to CSV
    df.to_csv('Section 18 - Motion Detector App/motion_records.csv')

    print("CSV saved successfully.")

    return df



def plotter(df):
    # Convert datetimes to strings
    df['Enter_str'] = df['Enter Time'].dt.strftime('%Y-%m-%d %H:%M:%S')
    df['Exit_str'] = df['Exit Time'].dt.strftime('%Y-%m-%d %H:%M:%S')

    # Extract data from DataFrame
    src = ColumnDataSource(df)

    # Creating figure object
    fg = figure(x_axis_type='datetime', height=200, width=1000, title="Motion Graph")

    # Modifying figure object
    fg.yaxis.minor_tick_line_color = None
    fg.ygrid.grid_line_color = None

    # Creating hover object
    hover = HoverTool(tooltips=[('Enter Time','@Enter_str'), ('Exit Time','@Exit_str')])
    fg.add_tools(hover)

    # Preparing data
    fg.quad(left='Enter Time', right='Exit Time', top=1, bottom=0, color='green', source=src)

    # Preparing output file
    output_file('Section 18 - Motion Detector App/motion_graph.html')
    
    # Saving output file
    save(fg)

    print("Motion graph saved successfully.")


if __name__ == '__main__':
    main()