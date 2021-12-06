import firebase from 'firebase/compat/app' //v9
import 'firebase/compat/firestore' //v9 
import 'firebase/compat/storage' //v9
import { getAnalytics } from "firebase/analytics";

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyC0dk94r2cJACfbqDRmTF51KyPAOsfNuT0",
  authDomain: "mvp-app-888ee.firebaseapp.com",
  projectId: "mvp-app-888ee",
  storageBucket: "mvp-app-888ee.appspot.com",
  messagingSenderId: "466727804062",
  appId: "1:466727804062:web:d988df6a2c1667ec006f8f",
  measurementId: "G-8FTSB30ZW4"
};

// Initialize Firebase
const app = firebase.initializeApp(firebaseConfig); 
const db = firebase.firestore(); 
const oStorage = firebase.storage();    
const analytics = getAnalytics(app);




export {db, oStorage};

