import firebase from 'firebase/compat/app' //v9
import 'firebase/compat/firestore' //v9 
import 'firebase/compat/storage' //v9
import { getAnalytics } from "firebase/analytics";

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
//  personal information deleted 
};

// Initialize Firebase
const app = firebase.initializeApp(firebaseConfig); 
const db = firebase.firestore(); 
const oStorage = firebase.storage();    
const analytics = getAnalytics(app);




export {db, oStorage};

