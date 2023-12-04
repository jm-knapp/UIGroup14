<template>
    <div class="section">
        <div class="container">
            <div class="columns is-centered">
                <div class="column is-one-third">
                    <div class="box">
                        <h1 class="title has-text-centered">Log in</h1>

                        <form @submit.prevent="submitForm">
                            <div class="field">
                                <label class="label">Username</label>
                                <div class="control has-icons-left">
                                    <input
                                        type="text"
                                        class="input"
                                        placeholder="Enter your username"
                                        v-model="username"
                                    />
                                    <span class="icon is-small is-left">
                                        <i class="fas fa-user"></i>
                                    </span>
                                </div>
                            </div>

                            <div class="field">
                                <label class="label">Password</label>
                                <div class="control has-icons-left">
                                    <input
                                        type="password"
                                        class="input"
                                        placeholder="Enter your password"
                                        v-model="password"
                                    />
                                    <span class="icon is-small is-left">
                                        <i class="fas fa-lock"></i>
                                    </span>
                                </div>
                            </div>

                            <div
                                class="notification is-danger"
                                v-if="errors.length"
                            >
                                <p v-for="error in errors" :key="error">
                                    {{ error }}
                                </p>
                            </div>

                            <div class="field">
                                <div class="control">
                                    <button
                                        class="button is-custom-button is-fullwidth"
                                    >
                                        Log in
                                    </button>
                                </div>
                            </div>

                            <hr />

                            <p class="has-text-centered">
                                Or
                                <router-link to="/sign-up">Sign up</router-link>
                                to create an account!
                            </p>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.section {
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}

.box {
    padding: 2rem;
    border-radius: 10px;
}

.button {
    margin-top: 10px;
}

.is-fullwidth {
    width: 100%;
}
.is-custom-button {
    background-color: #000000;
    color: #ffffff;
    border-color: transparent;
}
</style>

<script>
import axios from "axios";

export default {
    name: "LogIn",
    data() {
        return {
            username: "",
            password: "",
            errors: [],
        };
    },
    mounted() {
        document.title = "Log In <> Game Item Shop!";
    },
    methods: {
        async submitForm() {
            axios.defaults.headers.common["Authorization"] = "";

            localStorage.removeItem("token");

            const formData = {
                username: this.username,
                password: this.password,
            };

            await axios
                .post("/api/v1/token/login/", formData)
                .then((response) => {
                    const token = response.data.auth_token;

                    this.$store.commit("setToken", token);

                    axios.defaults.headers.common["Authorization"] =
                        "Token " + token;

                    localStorage.setItem("token", token);

                    const toPath = this.$route.query.to || "/cart";

                    this.$router.push(toPath);
                })
                .catch((error) => {
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.errors.push(
                                `${property}: ${error.response.data[property]}`
                            );
                        }
                    } else {
                        this.errors.push(
                            "Something went wrong. Please try again"
                        );
                        notificationAlert('Something went wrong and an error occurred. Please try again.')

                        console.log(JSON.stringify(error));
                    }
                });
        },
    },
};

function notificationAlert(message){
    let liveRegion = document.getElementById('live-region');
    liveRegion.textContent = message;
    liveRegion.setAttribute('aria-live', 'assertive');
    liveRegion.focus();
}
</script>
