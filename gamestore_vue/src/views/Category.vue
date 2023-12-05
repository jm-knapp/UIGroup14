<template>
    <div class="page-category">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h2 class="is-size-2 has-text-centered">{{ category.name }}</h2>
                <div class="field">
                    <label class="label">Sort by:</label>
                    <div class="control">
                        <div class="select">
                            <select v-model="sortOption" @change="sortProducts">
                                <option value="highestToLowest">
                                    Price : High To Low
                                </option>
                                <option value="lowestToHighest">
                                    Price : Low To High
                                </option>
                            </select>
                        </div>
                    </div>
                </div>
            </div>

            <ProductBox
                v-for="product in sortedProducts"
                :key="product.id"
                :product="product"
            />
        </div>
    </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";

import ProductBox from "@/components/ProductBox";

export default {
    name: "Category",
    components: {
        ProductBox,
    },
    data() {
        return {
            category: {
                products: [],
            },
            sortOption: "highestToLowest", // Set default to 'highestToLowest'
        };
    },
    mounted() {
        this.getCategory();
    },
    watch: {
        $route(to, from) {
            if (to.name === "Category") {
                this.getCategory();
            }
        },
    },
    computed: {
        sortedProducts() {
            const sorted = [...this.category.products];
            if (this.sortOption === "lowestToHighest") {
                sorted.sort((a, b) => a.price - b.price);
                notificationAlert('Sorted lowest to highest')
            } else if (this.sortOption === "highestToLowest") {
                sorted.sort((a, b) => b.price - a.price);
                notificationAlert('Sorted highest to lowest')
            }
            return sorted;
        },
    },
    methods: {
        async getCategory() {
            const categorySlug = this.$route.params.category_slug;

            this.$store.commit("setIsLoading", true);

            axios
                .get(`/api/v1/products/${categorySlug}/`)
                .then((response) => {
                    this.category = response.data;
                    document.title = this.category.name + " <> Game Item Shop!";
                })
                .catch((error) => {
                    console.log(error);

                    toast({
                        message: "Something went wrong. Please try again.",
                        type: "is-danger",
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: "bottom-right",
                    });
                });

            this.$store.commit("setIsLoading", false);
        },
        sortProducts() {
            // Triggered when the sorting option changes
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
