<template>
    <div id="wrapper">
        <nav class="navbar is-dark">
            <div class="navbar-brand">
                <router-link to="/" class="navbar-item" id="nav-name"
                    ><strong>Game Shop!</strong></router-link>

                <a
                    class="navbar-burger"
                    aria-label="menu"
                    aria-expanded="false"
                    data-target="navbar-menu"
                    @click="showMobileMenu = !showMobileMenu"
                >
                    <span aria-hidden="true"></span>
                    <span aria-hidden="true"></span>
                    <span aria-hidden="true"></span>
                </a>
            </div>

            <div
                class="navbar-menu"
                id="navbar-menu"
                v-bind:class="{ 'is-active': showMobileMenu }"
            >
                <div class="navbar-start">
                    <div class="navbar-item"></div>
                </div>
                <div class="navbar-mid is-flex is-align-items-center">
                    <form method="get" action="/search">
                        <div class="field has-addons">
                            <div class="control">
                                <input
                                    type="text"
                                    class="input"
                                    placeholder="Search!"
                                    name="query"
                                    style="width: 500px"
                                    aria-label="Input search field"
                                />
                            </div>

                            <div class="control">
                                <button class="button is-custom-search-button" aria-label="Search">
                                    <span class="icon">
                                        <i class="fas fa-search"></i>
                                    </span>
                                </button>
                            </div>
                        </div>
                    </form>
                </div>

                <div class="navbar-end">
                    <div class="navbar-item has-dropdown is-hoverable" aria-describedby="Categories dropdown list">
                        <a class="navbar-link"> Categories </a>

                        <div class="navbar-dropdown">
                            <router-link to="/AllProducts" class="navbar-item" aria-describedby="All Products Category"
                                >All Products</router-link>
                            <router-link to="/Cosmetics" class="navbar-item" aria-describedby="Cosmetic Items Category"
                                >Cosmetics</router-link>
                            <router-link to="/Boosts" class="navbar-item" aria-describedby="Boost Items Category"
                                >Boosts</router-link>
                            <router-link to="/Consumables" class="navbar-item" aria-describedby="Consumable Items Category"
                                >Consumables</router-link>
                            <router-link to="/weapons" class="navbar-item" aria-describedby="Weapons Category"
                                >Weapons</router-link>
                        </div>
                    </div>

                    <div class="navbar-item">
                        <div class="buttons">
                            <template v-if="$store.state.isAuthenticated">
                                <router-link
                                    to="/my-account"
                                    class="button is-light"
                                    >My Account</router-link
                                >
                            </template>
                            <template v-else>
                                <router-link
                                    to="/log-in"
                                    class="button is-light"
                                    >Log in</router-link
                                >
                            </template>

                            <router-link
                                to="/cart"
                                class="button is-custom-search-button"
                                >Cart ({{ cartTotalLength }})</router-link>
                        </div>
                    </div>
                </div>
            </div>
        </nav>

        <div
            id="live-region" 
            class="is-loading-bar has-text-centered"
            v-bind:class="{ 'is-loading': $store.state.isLoading }"
        >
            <div class="lds-dual-ring"></div>
        </div>

        <section class="section">
            <router-view />
        </section>

        <footer class="footer">
            <p class="aboutlink"><router-link to="/about">About This Site!</router-link></p>
            <p class="has-text-centered">Copyright (c) 2023</p>
        </footer>
    </div>
</template>

<script>
import axios from "axios";

export default {
    data() {
        return {
            showMobileMenu: false,
            cart: {
                items: [],
            },
        };
    },
    beforeCreate() {
        this.$store.commit("initializeStore");

        const token = this.$store.state.token;

        if (token) {
            axios.defaults.headers.common["Authorization"] = "Token " + token;
        } else {
            axios.defaults.headers.common["Authorization"] = "";
        }
    },
    mounted() {
        this.cart = this.$store.state.cart;
    },
    computed: {
        cartTotalLength() {
            let totalLength = 0;

            for (let i = 0; i < this.cart.items.length; i++) {
                totalLength += this.cart.items[i].quantity;
            }

            return totalLength;
        },
    },
};
</script>

<style lang="scss">
@import "../node_modules/bulma";

.aboutlink{
  text-align: center;
}
.lds-dual-ring {
    display: inline-block;
    width: 80px;
    height: 80px;
}
.lds-dual-ring:after {
    content: " ";
    display: block;
    width: 64px;
    height: 64px;
    margin: 8px;
    border-radius: 50%;
    border: 6px solid #ccc;
    border-color: #ccc transparent #ccc transparent;
    animation: lds-dual-ring 1.2s linear infinite;
}
#navbar-menu {
    background-color: #000000;
}
#nav-name {
    background-color: #000000;
}
.is-custom-search-button {
    background-color: #6ccbf6;
    color: #ffffff;
    border-color: transparent;
}

@keyframes lds-dual-ring {
    0% {
        transform: rotate(0deg);
    }
    100% {
        transform: rotate(360deg);
    }
}

.is-loading-bar {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 0;
    overflow: hidden;

    -webkit-transition: all 0.3s;
    transition: all 0.3s;

    &.is-loading {
        height: 80px;
    }
}
</style>
