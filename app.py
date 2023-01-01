import streamlit as st
import pandas as pd
import plotly_express as px


# DB Management
import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()







def mainprog():





    # st.title("Advance Data Visualization App")
    st.subheader("Welcome User")
    # Add a sidebar
    st.sidebar.subheader("Visualization Settings")

    # Setup file upload
    uploaded_file = st.sidebar.file_uploader(label="upload your CSV file.",
                                             type=['csv'])

    global df
    global clean
    if uploaded_file is not None:
        print(uploaded_file)
        print("hello")
        try:
            df1 = pd.read_csv(uploaded_file)
            df = df1.fillna(df1.mean())
            st.sidebar.subheader("Cleaning OF Data")
            clean = st.sidebar.selectbox( label = "Select the cleaning method",
                                          options=['Remove the Null','Fill NA mean','Fill NA with Median',
                                                   'Fill NA with Mode','label_encoder',])


        except Exception as e:
            print(e)
            df1 = pd.read_excel(uploaded_file)
            df=df1.fillna(df1.mean())

    global numeric_columns
    try:
        st.write(df)
        totalrows = f'Total no of Rows = {df.shape[0]}'
        totalcols = f'Total no of Columns = {df.shape[1]}'
        st.write(totalrows)
        st.write(totalcols)
        st.write(df.describe())
        numeric_columns = list(df.select_dtypes(['float', 'int']).columns)
    except Exception as e:
        print(e)
        st.write("Please upload file to the application.")



    # add a select widget to the side bar
    st.sidebar.subheader("Select the Plot")
    chart_select = st.sidebar.selectbox(
        label="Select the chart type",
        options=['Scatterplots', 'Lineplots', 'Histogram', 'Boxplot', 'Scatterplot3d','Connected Scatterplots','Scatterplot discretecolor','scatter_matrix','Violin','Histogram_pattern','Scatterplot_hover','Histogram_color']
    )

    if chart_select == 'Scatterplots':
        st.sidebar.subheader("Scatterplots"
                             ""
                             ""
                             " Settings")
        try:
            x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
            y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)

            plot = px.scatter(data_frame=df, x=x_values, y=y_values)

            # display the chart
            st.plotly_chart(plot)

        except Exception as e:
            print(e)

    if chart_select == 'Scatterplot3d':
        st.sidebar.subheader("Scatterplot3d Settings")
        try:
            x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
            y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
            z_values = st.sidebar.selectbox('Z axis', options=numeric_columns)
            plot = px.scatter_3d(data_frame=df, x=x_values, y=y_values, z=z_values)

            # display the chart
            st.plotly_chart(plot)

        except Exception as e:
            print(e)

    if chart_select == 'Lineplots':
        st.sidebar.subheader("Lineplot Settings")
        try:
            x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
            y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
            color = st.sidebar.selectbox('Z axis', options=numeric_columns)
            plot = px.line(data_frame=df, x=x_values, y=y_values, color=color)

            # display the chart
            st.plotly_chart(plot)

        except Exception as e:
            print(e)

    if chart_select == 'Boxplot':
        st.sidebar.subheader("Boxplot settings")
        try:
            x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
            y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
            plot = px.box(data_frame=df, x=x_values, y=y_values)

            # display the chart
            st.plotly_chart(plot)

        except Exception as e:
            print(e)

    if chart_select == 'Histogram':
        st.sidebar.subheader("Boxplot settings")
        try:
            x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
            #y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
            plot = px.histogram(data_frame=df, x=x_values)

            # display the chart
            st.plotly_chart(plot)

        except Exception as e:
            print(e)

    if chart_select == 'Histogram_pattern':
        st.sidebar.subheader("Histogram settings")
        try:
            x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
            y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
            z_values = st.sidebar.selectbox('z_axis', options=numeric_columns)
            a_values = st.sidebar.selectbox('a_axis',options=numeric_columns)
            plot = px.histogram(data_frame=df, x=x_values,y=y_values,color=z_values,pattern_shape=a_values)

            # display the chart
            st.plotly_chart(plot)

        except Exception as e:
            print(e)

    if chart_select == 'Connected Scatterplots':
        st.sidebar.subheader("Connected Scatterplot settings")
        try:
            x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
            y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
            z_values = st.sidebar.selectbox('Color', options=numeric_columns)
            a_values = st.sidebar.selectbox('Text', options=numeric_columns)
            plot = px.line(data_frame=df, x=x_values, y=y_values, color=z_values,text=a_values)

            # display the chart
            st.plotly_chart(plot)

        except Exception as e:
            print(e)

    if chart_select == 'Violin':
        st.sidebar.subheader("Violin settings")
        try:
            x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
            y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
            z_values = st.sidebar.selectbox('Color', options=numeric_columns)

            plot = px.violin(data_frame=df, x=x_values, y=y_values, color=z_values,box=True, points='all', hover_data=df.columns)

            # display the chart
            st.plotly_chart(plot)

        except Exception as e:
            print(e)


    if chart_select == 'Scatterplot discretecolor':
        st.sidebar.subheader("Scatterplot settings")
        try:
            x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
            y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
            z_values = st.sidebar.selectbox('Color', options=numeric_columns)

            plot = px.scatter(data_frame=df, x=x_values, y=y_values, color=z_values)

            # display the chart
            st.plotly_chart(plot)

        except Exception as e:
            print(e)

    if chart_select == 'Histogram_color':
        st.sidebar.subheader("Boxplot settings")
        try:
            x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
            y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
            plot = px.histogram(data_frame=df, x=x_values,color=y_values)

            # display the chart
            st.plotly_chart(plot)

        except Exception as e:
            print(e)

    if chart_select == 'Scatterplot_hover':
        st.sidebar.subheader("Scatterplot_hover settings")
        try:
            x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
            y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
            a_values = st.sidebar.selectbox('z_axis',options=numeric_columns)
            d_values = st.sidebar.selectbox('d_axis', options=numeric_columns)
            z_values = st.sidebar.selectbox('Color', options=numeric_columns)


            plot = px.scatter(data_frame=df ,x=x_values, y=y_values, size=d_values, color=z_values, hover_name=a_values, log_x=True, size_max=60)

            # display the chart
            st.plotly_chart(plot)

        except Exception as e:
            print(e)







# Security
#passlib,hashlib,bcrypt,scrypt
import hashlib
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False






def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data



def main():
	"""Simple Login App"""

	st.title("ADVANCE DATA ANALYZER")

	menu = ["Login","SignUp"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Login":
		# st.subheader("Login Section")

		username = st.sidebar.text_input("User Name")
		password = st.sidebar.text_input("Password",type='password')
		if st.sidebar.checkbox("Login"):
			# if password == '12345':
			create_usertable()
			hashed_pswd = make_hashes(password)

			result = login_user(username,check_hashes(password,hashed_pswd))
			if result:
				mainprog()
				# st.success("Logged In as {}".format(username))
				#
				# task = st.selectbox("Task",["Add Post","Analytics","Profiles"])
				# if task == "Add Post":
				# 	st.subheader("Add Your Post")
				#
				# elif task == "Analytics":
				# 	st.subheader("Analytics")
				# elif task == "Profiles":
				# 	st.subheader("User Profiles")
				# 	user_result = view_all_users()
				# 	clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
				# 	st.dataframe(clean_db)
			else:
				st.warning("Incorrect Username/Password")





	elif choice == "SignUp":
		st.subheader("Create New Account")
		new_user = st.text_input("Username")
		new_password = st.text_input("Password",type='password')

		if st.button("Signup"):
			create_usertable()
			add_userdata(new_user,make_hashes(new_password))
			st.success("You have successfully created a valid Account")
			st.info("Go to Login Menu to login")








if __name__ == '__main__':
	main()