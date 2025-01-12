---
title: Development of a Reward Selector App for iOS
start_date: 09-04-2024
end_date: Current
brief: I created an iOS application using React Native that allows users to define and randomly select rewards based on calculated probabilities, improving decision-making processes with a user-friendly interface and efficient backend logic.
---
Robert is planning to create an iOS application using React Native. The app is designed to randomly select rewards, with functionality for users to add items with associated values that determine the item's selection probability using a formula (40/value). The app's main features include adding items and a random selection mechanism where probabilities are dynamically calculated based on the items' values. Initially, the app will have minimal components, including buttons for adding items and making selections. There are no specific target audience limitations, and no external tools or integrations are required.


####: Content
App Description:
Name: Reward Selector
Platform: iOS
Development Framework: React Native

Purpose:
The Reward Selector app is designed to randomly select rewards based on user-defined probabilities. It allows users to add rewards (items) with associated values, which then influence the likelihood of each item being selected during a random draw.

Target Audience:
The app is suitable for a broad audience, making it a versatile tool for anyone interested in random selection for rewards or decision-making.

Key Features:
Adding Items:

Interface: Simple form with fields for item name and value.
Functionality: Users can add items to the pool. Each item's selection probability is calculated as 40/value. This value determines how likely it is to be selected relative to other items.
Random Selection:

Button: A dedicated button to initiate the random selection process.
Algorithm: The app calculates the probability for each item based on its value and performs a random draw. The draw might result in selecting one of the items or none, based on calculated probabilities.
User Interface:
Main Screen:
Add Item Button: Opens a form to enter the name and value of a new item.
Random Select Button: Executes the random selection process and displays the result.
Development Instructions:
Setup React Native Environment:

Ensure you have Node, Watchman, the React Native command line interface, Xcode, and CocoaPods installed.
Set up a new React Native project using npx react-native init RewardSelector.
Developing the Interface:

Create a simple UI with two buttons and input forms using React Native components like Button, TextInput, and View.
Implementing the Logic:

Use JavaScript for the logic to add items and calculate probabilities. Store items in state using useState.
Implement the random selection function using JavaScript's Math.random() to decide based on the defined probabilities.
Testing:

Test the app on iOS simulators in Xcode to ensure functionality across different devices.
Deployment:

Once testing is completed, use Xcode to build the app and deploy it to the App Store.
This structure provides a clear path from concept to deployment for your Reward Selector app. If you need further details on any part of the process, feel free to ask!




