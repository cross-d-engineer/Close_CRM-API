# Working wiith Close_CRM-API

<h2>Project Overview</h2>
<p>This script was created with the expectation of the following are already in place:</p>
<ol>
    <li>You already have git and python 3.9.</li>
    <li>You have already <a href="https://app.close.com/signup">registered</a> with your email address for an account.</li>
    <li>You have already <a href="https://help.close.com/docs/api-keys">generated a Close API key</a>.</li>
    <li>You have access to this CSV file: <a href="https://docs.google.com/spreadsheets/d/1omg1_ZSCMlTLzwv9tON7pkGU10_rDOeJeKmTi_qtf-k/edit?usp=sharing">CSV file</a>.</li>
</ol>
</br>
<h2>Running The Script</h2>
<h3>Script Pre-requisites</h3>
<p>Before running the script please ensure that:</p>
<ol>
    <li>To properly install the required dependencies, make sure to execute the command <b>"pip install -r requirements.txt"</b> while inside the virtual environment.</li>
    <li>The 'main.py' file, its associated modules, and the CSV file are located in the same local directory.</li>
</ol>
<p>Upon execution of the script, the console will provide prompts for required user information, such as;</p>
<ol>
    <li>API Key</li>
    <li>Filename</li>
    <li>Filter Start and End dates as well as records limit.</li>
</ol>
<h2>How the Script Works</h2>
<p>
During the execution of the script, the console would show <b>Validation errors</b> for invalid data that was caught while importing the lead data into the organization. Validation of data is handled when a POST is done to <b>Close.com API</b> which returns an error if invalid data is provided.
<pre>
<img src="https://github.com/cross-d-engineer/Close_Take_Home_Assignment/blob/main/src_imgs/validation_error_sample.png">
</pre>
When invalid data is received the <b>Close API Client</b> returns an error message which halts the execution of the script. To bypass the error report, the "<span style="color: rgb(255, 174, 0);">try</span>" and “<span style="color: rgb(255, 174, 0);">except</span>” block is used to continue the execution.
<pre>
<img src="https://github.com/cross-d-engineer/Close_Take_Home_Assignment/blob/main/src_imgs/try_except_sample.png">
</pre>
</p>
</pre>
To find the leads within the given range, in the prompt mentioned above, a JSON query was created using the Close Visual Query Builder to determine the filter structure. 
That query was populated with the values captured including the <span style="color: rgb(0, 255, 157);">“_limit: number”</span> field which controls the number of records returned as well as the <span style="color: rgb(0, 255, 157);">“_field:__”</span> field which provides more of the data from the object queried.</p>
<pre>
  <img src="https://github.com/cross-d-engineer/Close_Take_Home_Assignment/blob/main/src_imgs/after_filter.png" alt="after_filter"> <img src="https://github.com/cross-d-engineer/Close_Take_Home_Assignment/blob/main/src_imgs/before_filter.png" alt="before_filter"> <img src="https://github.com/cross-d-engineer/Close_Take_Home_Assignment/blob/main/src_imgs/limit_filter.png" alt="limit_filter">
</pre>
</br>
<p>Using the filtered data response, the leads are then segmented using a series of loops that iterate through the response to extract the data and then place them in python dictionaries. </p>
</br>
<p>To determine and segment the leads by State the script creates a dictionary that maps the values to keys labeled as the states and nests the corresponding values within ensuring there are no conflicts or overwrites by using conditional logic to determine which states have been already created as well as the lead with the most revenue within said state. </p>
<pre>
<img src="https://github.com/cross-d-engineer/Close_Take_Home_Assignment/blob/main/src_imgs/data_segmentation.png">
<img src="https://github.com/cross-d-engineer/Close_Take_Home_Assignment/blob/main/src_imgs/data_segmentation2.png">
</pre>
</br>
<p>The median is found using a conditional to determine whether the total list of numbers are odd or even. If odd list of numbers would be sorted and divided by 2 to determine its location within the list. If even the middle 2 numbers of the list were added and then divided by 2.</p>
<img src="https://github.com/cross-d-engineer/Close_Take_Home_Assignment/blob/main/src_imgs/the_median.png">
</br>
<p>There are two local modules created to work with this script “data.py” which holds and the query structures used for interacting with the API and <b>“prep_csv.py”</b> which is responsible for processing the data described above to be written to csv.</p>
<p> At the end of the script two files should be written to your repository. One of the files would be named "Lead_Error_Logs.csv" which provides all logs captured whilst running the script. The other would be the final output containing the information requested and would be named "Project_Output.csv" within the local repository.
</p>
<pre>
<img src="https://github.com/cross-d-engineer/Close_Take_Home_Assignment/blob/main/src_imgs/output.jpg", alt='final_output_sample'>
</pre>
