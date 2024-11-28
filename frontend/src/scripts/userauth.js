import { ref } from "vue";
import { defineStore } from "pinia";
import api from "./axios";
import axios from "axios";

export const useUserAuthStore = defineStore("auth", () => {
  const token = ref(null);
  const user = ref(null);

  async function authLogin(email, password) {
    try {
      const response = await api.post("api/login/", {
        email: email,
        password: password,
      });
      token.value = response.data.access;
      localStorage.setItem("token", token.value);
      api.defaults.headers.common["Authorization"] = `Bearer ${token.value}`;
      return true;
    } catch (error) {
      console.error("Error logging in:", error);
      throw error;
    }
  }

  async function authRegister(fullNames, email, password) {
    try {
      const response = await axios.post("https://taakarwanda.pythonanywhere.com//api/register/", {
        fullNames: fullNames,
        email: email,
        password: password,
      });
    } catch (error) {
      console.error("Error registering:", error);
    }
  }
  async function authLogout() {
    token.value = null;
    localStorage.removeItem("token");
    delete api.defaults.headers.common["Authorization"];
  }

  //
  return {
    token,
    user,
    authLogin,
    authRegister,
    authLogout,
  };
});
