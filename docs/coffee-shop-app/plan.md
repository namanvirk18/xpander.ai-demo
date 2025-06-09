 # Coffee Shop Mobile App - Planning

 ## Figma Design Analysis

 **Screens:**
 - Splash / Onboarding Screen
 - Sign In / Sign Up Screen
 - Home / Feed Screen
 - Menu / Product List Screen
 - Product Detail Screen
 - Cart Screen
 - Checkout / Order Confirmation Screen
 - Community Feed Screen
 - Community Post Detail Screen
 - New Community Post Screen
 - User Profile Screen
 - Settings Screen

 **Components:**
 - Header (with back button, title)
 - Footer / Bottom Navigation Bar
 - Card (product, community post)
 - Button (primary, secondary)
 - Avatar / User Thumbnail
 - Icon (social, navigation)
 - Tab Bar / Tabs
 - Input Field (text, search)
 - Modal (confirmation, form)
 - Badge (notification count)
 - Rating Stars
 - Loading Spinner

 **Assets:**
 - Brand logo (SVG / PNG)
 - Product images (JPEG / PNG placeholders)
 - Community user avatars
 - Background illustrations
 - Icon set (SVG / PNG)
 - Fonts (e.g., custom headings)

 ## Folder Structure

 ```
 coffee-shop-app/
 ├── src/
 │   ├── assets/
 │   │   ├── fonts/
 │   │   ├── images/
 │   │   └── icons/
 │   ├── components/
 │   ├── navigation/
 │   ├── screens/
 │   ├── hooks/
 │   ├── context/
 │   ├── services/
 │   └── utils/
 ├── .gitignore
 ├── App.js
 ├── package.json
 └── README.md
 ```

 ## Dependencies

 - **Navigation:** @react-navigation/native, @react-navigation/bottom-tabs, @react-navigation/stack
 - **Gesture & Animation:** react-native-gesture-handler, react-native-reanimated
 - **Icons:** react-native-vector-icons
 - **Networking:** axios
 - **State Management:** context API (built-in) or optionally Redux / Zustand
 - **Forms & Validation:** formik, yup
 - **Styling:** styled-components or @emotion/native
 - **Other:** react-native-svg, react-native-safe-area-context

 *(Further adjustments once starting development)*