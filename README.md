Group 4:
200487463 - Sanket Borkar
200494051 - Jeegniben Patel
200484628 - Rahman Armaghan
200481510 - Gurkirat Singh Saini
200481194 - Anjani Sonavane 

UNDERSTANDING THE PROBLEM
 Due to the continuous growth of autonomous vehicles, many countries started facing 
challenges related to environmental pollution, traffic congestion, not enough parking, 
accidents, as well as other inevitable problems. For example, a car with the ability to carry 5 
people in full capacity, which is used to travel by and only for one person, 80% of the car 
capacity and fuel is wasted during individual travel. The major problems are cost and timing. 
If a person opts for public transportation, it takes a longer time to reach the destination, 
sometimes they have to walk a lot to go to the bus stop/railway station and switch the 
transportation medium in the route, likewise if they choose cab, the cost will go beyond a 
normal limit, moreover for the daily transportation, the cab option is not feasible for some 
people, such as students. There is also a possibility that during ride sharing, the preferences of 
driver and rider doesn’t match, such as gender issue, music required or not and many more. 
Sometimes, driver struggles to find the shortest and quick route. As the fuel prices increasing, 
cost of ride for a single person/driver could be more. In ride sharing, it would be time 
consuming to add many details every time in app/website. If the journey is too long, it would 
be boring or depressing for some people to travel alone. Many of us always try to find similar 
faces during our day to get a normal smile on our faces. 
IDENTIFYING THE PROJECT REQUIREMENT
 The best solution to reduce the number of vehicles on the street is ‘Smart Ride Sharing’, 
which is also known as carpooling. In ride sharing, people who are going to their college/office 
and have almost similar timeslot and same route such that they can share a car, which is owned 
by a driver, in short, we share empty vehicle seats with people (known or unknown, but 
verified). There are few AI algorithms that we can use to find the shortest route and best path 
3
to travel. The driver shares their own car with people, who have the same or on the way source 
and destination. By smart sharing, we can reduce the traffic, pollution, less time to travel and 
most importantly cost effective for both driver/owner and rider.
 We can add preferences such as gender, type of music during travel, smoker or not, riders 
review, cost, talkative and many more and by having these data, we can try to find the best 
possible travel companions using AI algorithms. Smart ride would be beneficial for both driver 
and rider as they both get paid. The driver can utilise that money in fuel and the rider can travel 
with less amount of money in a short interval. We can build app/website so that people can 
navigate through it. By Ride sharing, person can find travel partners to share their journey, 
which could be joyful and supportive.
 Here, to make Ride sharing smarter, we are planning to use a speech/text chatbot using 
speech/text recognition. With just a click or speech, a driver can inform their start time and the 
rider can also get an update. Rider can get options based on the predictions using AI algorithms 
of their selection. The actual model is based on real time data, but during our development, we 
can use some pre-defined data to train the model. The driver can see the prediction also, on 
which time and using which route they can get more riders, same applies to rider, so that they
can pre-plan their journey. The system learns about destinations and preferences from GPS 
traces and calendars and considers time, fuel, environmental, and cognitive costs using 
algorithms. For trust and comfort issues, we can add filter for gender and co-worker also.
 If there are multiple drivers with good matches available, how can we train our model 
with AI/ML, such as which driver to show on priority? Who will accept the request? What is 
the probability that driver will send a request or a driver will send that?
4
IDENTIFYING COMPUTING RESOURCES AND PROPOSED FRAMEWORK
 We would be needed a specific cost function to predict the cost of a ride before travel. 
Sometimes it is difficult to predict cost as journey is based on travel kilometres and number of 
riders and drivers available, demand of driver’s foe specific route, traffic which causes last time 
to change of route, etc.
 There is Multiple-Sources-Multiple-Destinations (MSMD) approach available, which is 
an excellent choice for Car-Pooling to complete a trip with appropriate time management. The 
main idea of designed model is to match riders based on human characteristics and the User 
Threshold Time (UTT). One more is a cloud computing framework for real-time carpooling 
services.
 We are planning to develop Deep-Pool framework to solve vehicles dispatch and routing 
issues. First mathematically characterize the objective function and its components. Deep-Pool 
framework is a model-free technique where future demands and customer statistics are taught 
to efficiently solve dispatch and routing problems in a distributed way utilising deep QNetwork for each vehicle. For individual vehicles, the reward will be learned from the 
environment and then used by system optimizer to optimise Deep-Pool framework.
 For future Demand prediction, we can use a convolutional neural network to predict 
demand. The below Flow diagram describes execution steps of system. The execution starts 
from finding/showing rider request and follows by allocating a driver, executing matching 
layers, recording rider feedback, and computing two main characteristics. The final step is to 
predict two main characteristics based on trained and tested Machine Learning classifier for 
newly registering riders.
 The Ride sharing model will include technology with two matching layers. The model 
will begin with rider registration for which we can use text based Chatbot also, where users 
5
provide required profile data along with specific details which can include positive digits on a 
scale of 1 to 5. The rider/driver selected in system is talkative, friendly, safe, on time, and 
comfortable. Once a driver/rider register in system, proposed model searches and matches 
riders having a similar set of characteristics. The matching of riders using these characteristics 
shows on priority.
 The travelling time between locations of broadcasting rider and other riders is computed 
using the Google Maps APIs and verified if calculated time is less than trip time expected. If 
riders satisfy matching layer conditions, the system adds them onto the final trip itinerary, 
marking completion of trip formation.
 After the trip completion, a user can see the feedback system begins where riders rate 
the driver as well as other riders on the trip. The feedback given by a user forms an essential 
data-set as the system uses feedback data to compute two main characteristics for every user. 
The determined characteristics are later employed by Machine Learning algorithms to predict 
better rider recommendations.
 The two determined characteristics are Feedback-Given-Characteristic and FeedbackReceived-Characteristic. Feedback-Given-Characteristic is derived based on feedback rider 
gives to other riders, while Feedback-Received-Characteristic is computed based on feedback 
rider gets from other riders. Two main characteristics are used to determine characteristics a 
rider most focuses on a trip while rating other riders. In the end, based on feedback patterns in 
past trips, system assigns the two most favoured characteristics to every rider.
 The computations for determining main characteristics of a rider are quite complex and 
tediously high. Thus, after recording enough trip and feedback records, we can use Machine 
Learning classification algorithms or classifiers to predict main characteristics of a rider, which 
eliminates need for complex computations. Machine Learning (ML) is a technology where a 
6
system learns, and trains based on an existing data-set and predicts outputs for new input data. 
In case of the Ride Sharing model, the thesis employs the Support Vector Machine (SVM) 
classification algorithm. After appropriate training and testing, SVM classifier predicts two 
main characteristics of newly registering riders. Riders are recommended based on predicted 
main characteristics. PFB the Flow Diagram.
 No
 Yes
 
Rider Request
Show nearest 
Driver Details
Search Riders 
based on entered 
characteristics
Filter Riders according 
to requirements
Available 
Vehicle 
Seats==0
Start &
Complete trip
Get review
using Chatbot
Predict Two 
main 
characteristics
Train and Test Machine 
learning Classifier
New Registered 
Driver/Riders
Chatbot
Predict Characteristics 
using ML Classifier
Find Riders based on 
Predictions
Complete Trip
7
MACHINE LEARING MODULE SELECTION
 In the ML-based recommendation system, the features are converted to vectors and 
represented in a d-dimensional space, where d is the number of features. The angular distance 
or the Cosine of the angle θ, which is between the vectors is calculated using the equation of 
the Dot Product. We will use a similar methodology where the selected features will be used 
as the registered rider characteristics.
 In Machine Learning algorithms we will do the prediction of the two main characteristics 
of newly registering riders. There could be a little error due to the presence of the imbalanced 
feedback data-set. In the case of an imbalanced data-set, for similar inputs, different outputs 
may be recorded, creating uncertainties during predictions. We need to find the Machine 
Learning classification algorithm or a classifier that could appropriately fit an imbalanced dataset and give quality predictions.
 We will work for a suitable Machine Learning classifier that can be used on the training 
and testing of feedback datasets with classifiers like Logistic Regression, K-Nearest 
Neighbours (KNN) classifier, Naive Bayes Multinomial classifier, Random Forests classifier, 
Neural Networks, and Support Vector Machine (SVM).
We are planning to implement text/speech based chatbot for more convenient use.
DETERMINING POSSIBLE ALGORITHM, METHODOLOGY, PROJECT 
MANAGEMENT, TOOLS, AND RESPONSIBILITY
 We are planning to execute “The Ridesharing” software invented and developed in the 
Django framework using Google Maps API. There will be a two-stage distributed estimation 
8
algorithm which helps to solve ridesharing problem. In the first stage rideshare factor (such as 
route, distance, and time) will be cluster. In the second stage according to result of clustering, 
the algorithm of matching, multi-objective programming, and intelligent algorithms would be
used to solve combinatorial problem. 
 We will check classical clustering algorithm, which comprises the k-means algorithm, 
fuzzy C-means (FCM) clustering algorithm, and hierarchical clustering algorithm, and the 
advance algorithm which can be used for comparative analysis.
 The Rideshare service will made solely available on the smartphone and possible on 
Android and Apple. This application might be continuously collects and measures all short 
distance trips (with all purpose) entered by user (in time and space) which would be convenient 
to understand user’s versatility habits and predict upcoming movement. The user will decide 
his/her role in the rideshare from the three possibilities: driver, passenger, or either (driver or 
passenger). With the knowledge, the application will automatically provide simple ridesharing 
opportunities for adjacent three destinations. The user, for whatever role he/she wish, will saw 
a list of opportunities and propose to make an appeal to another user. These possibilities will
show outdoors either driver or rider confirming that the prophesied trip would transpire. It will 
be also possible to manually add unpredicted trips. The travel time used for matching and 
9
presented to users will be estimated based on an ordinary time/kilometre/type of geographic 
area (urban or rural). Every user will be having a profile with different obligatory and 
unrestricted data possibilities (first name, photo, preferences, peer evaluations, company for 
the users working for a corporate customer of the app). A chat option will also be made feasible
for communication purposes (talk/query) with other users or with Audrey, the customer service 
representative.
BUILDING TRAINING TESTING THE MODEL
For the Ride sharing model, we are planning to implement a speech/text based chatbot and 
predefined data set at the initial stage for training and testing. If time permits, we will 
implement a pilot application or website for user-friendly experience. The application may 
provide functionalities like rider registration, broadcasting a request, completing a trip, and 
rating other users. As of now, we are not including billing part in this model, but we will try to 
cover cost predictions based on the factors such as travel distance and others, as mentioned
above.
We are going to use an Agile software development life cycle where requirements, 
programming, and testing are often done concurrently. Please find below the planned steps:
1) We will try to meet all the requirements and develop the model as per desire.
2) Respond correctly to all kinds of inputs.
• Self – Review
• Peer – Review
• Unit Testing
3) Perform its functional requirement within an acceptable time.
10
• Integration testing
• Regression testing
❖ Plan Visualization and Creation of Issues:
1) The visualizer supports the following functionalities:
• Create ride sharing scenarios.
• Solve ride sharing scenarios.
• Add adaptation issues (blocked streets) by clicking on a street.
• Visualize the solutions step by step.
• Visualize the overall distance traversed by carpools and passengers.
2) The following list shows what each of the navigation buttons does:
• Play - each of step in the plan is automatically displayed one after the other. Each state 
is shown for one second.
• Pause - stops the automatic displaying of the plan.
• Next - shows the next state in the plan.
• Restart - resets the visualizer to the first state (blocked streets are kept).
• Generate scenario - generates a new carpooling scenario.
• Send current state - the current state of the scenario is sent to the solver to get an updated 
solution, e.g., to resolve new adaptation issues (blocked streets).
Refining the model
To meet requirements of the user and make the software secure as well as precise we will 
include features time to time. 
11
• The website should allow the users (ride-share members) to register themselves using 
their name, phone number, email address, driver’s license number, etc. which can be 
helpful from the security point of view
• We will use google API and collect the real time data of the traffic. In order to show 
the correct time of the ride and the fastest ride available to the ride share members.
• Based on daily availability of the rides on the set routes, we can predict the busy hours 
as well as no availability hours, which help members to book their rides in advance.
• We will include a feedback section in the software in order to rate the ride as well as 
ride sharer. The data will ultimately help in evaluating the customer in case of bias or 
dispute