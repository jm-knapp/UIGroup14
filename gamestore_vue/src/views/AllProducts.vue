<template>
    <div class="page-category">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h2 class="is-size-2 has-text-centered">All Products</h2>
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
    name: "AllProducts",
    components: {
        ProductBox,
    },
    data() {
        return {
            products: [],
            sortOption: "highestToLowest", // Set default to 'highestToLowest'
        };
    },
    mounted() {
        this.getAllProducts();
        document.title = "All Products <> Game Item Shop!";
    },
    computed: {
        sortedProducts() {
            const sorted = [...this.products];
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
        async getAllProducts() {
            this.$store.commit("setIsLoading", true);

            await axios
                .get("/api/v1/all-products/")
                .then((response) => {
                    this.products = response.data;
                })
                .catch((error) => {
                    console.log(error);
                });

            this.$store.commit("setIsLoading", false);
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