<script setup>
import { onMounted, reactive, ref } from "vue";
import api from "../scripts/axios";
import { useUserAuthStore } from "@/scripts/userauth";
import navigation from "@/components/navigation.vue";
import { useRouter } from "vue-router";

const router = useRouter();

let uploadName = ref("");
const uploadFile = ref(null);

//getting token
const UserAuthStore = useUserAuthStore();
// Display logged-in user's name
const user = ref([]);
async function UserDetails() {
  try {
    const response = await api.get("api/userdetails/", {
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${UserAuthStore.token}`,
      },
    });
    user.value = response.data; // Update user details in the state
    return user.value;
  } catch (error) {
    console.error("Error fetching user details:", error);
  }
}
onMounted(() => {
  UserDetails();
});

function upload(e) {
  uploadFile.value = e.target.files[0];
  uploadName.value = e.target.files[0].name;
}

const product = reactive({
  productName: "",
  productPrice: null,
});

async function uploadArtwork() {
  //check is there is a file selected
  if (!uploadFile.value) {
    alert("Please select a file first.");
    return;
  }

  const sendData = new FormData();
  sendData.append("productName", product.productName);
  sendData.append("productPrice", product.productPrice);
  sendData.append("productImage", uploadFile.value);

  try {
    const response = await api.post("/api/createproduct/", sendData, {
      headers: {
        "Content-Type": "multipart/form-data",
        Authorization: `Bearer ${UserAuthStore.token}`,
      },
    });
    if (uploadArtwork) {
      router.push("/shop");
    }
    console.log("Upload successful:", response.data);
  } catch (error) {
    console.error("Upload failed:", error);
  }
}
async function logOut() {
  try {
    await UserAuthStore.authLogout();
    if (logOut) {
      router.push("account/login");
    }
  } catch (error) {}
}
</script>

<template>
  <navigation />
  <section class="create-wrapper">
    <h4>wellcome back {{ user.fullNames }}</h4>
    <button @click="logOut">log out</button>
    <h4>create art work</h4>
    <div @change="upload" class="create-file">
      <span>file name: {{ uploadName }}</span>
      <label for="uploadfile" class="uploadfile">select file </label>
      <input type="file" id="uploadfile" accept="image/*" />
    </div>
    <form action="" class="file-upload-form" @submit.prevent="uploadArtwork">
      <input
        type="text"
        name="title"
        id="title"
        required
        placeholder="name of art work"
        v-model="product.productName"
      />

      <input
        type="number"
        name="price"
        id="price"
        required
        placeholder="price of art work"
        v-model="product.productPrice"
      />

      <input type="submit" required value="upload art work" class="form-cta" />
    </form>
  </section>
</template>

<style>
.create-wrapper {
  height: calc(100vh - 64px);
  margin-top: 64px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 8px;
  padding: 8px 144px;

  h4 {
    font-size: 16px;
    text-transform: capitalize;
  }

  button {
    font-size: 14px;
    cursor: pointer;
    text-decoration: underline;
  }

  .file-upload-form {
    display: flex;
    flex-direction: column;
    gap: 16px;
    width: 32vw;

    input {
      padding: 24px;
      border: 1.4px solid rgb(17, 0, 203);
      font-size: 16px;
      border-radius: 4px;
      text-transform: capitalize;
      color: rgb(17, 0, 203);
    }

    .form-cta {
      border: none;
      background-color: rgb(17, 0, 203);
      color: white;
      font-size: 16px;
      padding: 24px;
      text-transform: uppercase;
      text-align: center;
      cursor: pointer;
    }
  }

  .create-file {
    width: 32vw;
    height: 260px;
    border: 1.4px solid rgb(17, 0, 203);
    background-color: rgb(17, 0, 203, 0.1);
    border-radius: 4px;
    display: flex;
    gap: 16px;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    font-size: 16px;
    text-transform: uppercase;

    .uploadfile {
      padding: 8px 16px;
      background-color: #161616;
      text-transform: uppercase;
      font-size: 12px;
      color: aliceblue;
    }

    input {
      display: none;
    }
  }
}
</style>
