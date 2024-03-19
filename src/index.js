// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { DataSnapshot, getDatabase } from "firebase/database";

const firebaseConfig = {
  apiKey: "AIzaSyDMQ1VIraBAzxdeBtDxzuAFZSd40tqjlO8",
  authDomain: "cps-406-shops--salsa-studio.firebaseapp.com",
  databaseURL: "https://cps-406-shops--salsa-studio-default-rtdb.firebaseio.com",
  projectId: "cps-406-shops--salsa-studio",
  storageBucket: "cps-406-shops--salsa-studio.appspot.com",
  messagingSenderId: "540925147740",
  appId: "1:540925147740:web:8bc6c580ffc93e905b0499",
  measurementId: "G-PY1KBBNP6C"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const db = getDatabase(app);

const distanceRef = ref.db('users/TREASURER')
