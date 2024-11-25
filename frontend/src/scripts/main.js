//imports
import { createPinia } from "pinia";
import { createApp } from "vue";
import App from "../App.vue";
import router from "./routes";
import "../css/reset.css";

//app

const pinia = createPinia();
const app = createApp(App);

app.use(pinia);
app.use(router).mount("#app");
