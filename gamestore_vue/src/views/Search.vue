<template>
    <div class="page-search">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Search</h1>
                <h2 class="is-size-5 has-text-grey">
                    Search term: "{{ query }}"
                </h2>
                <div class="field">
                    <label class="label">Sort by:</label>
                    <div class="control">
                        <div class="select">
                            <select v-model="sortOption" @change="sortProducts">
                                <option value="lowestToHighest">
                                    Price : Low To High
                                </option>
                                <option value="highestToLowest">
                                    Price : High To Low
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
import ProductBox from "@/components/ProductBox.vue";

export default {
    name: "Search",
    components: {
        ProductBox,
    },
    data() {
        return {
            products: [],
            query: "",
            sortOption: "highestToLowest", // Set default to 'highestToLowest'
        };
    },
    mounted() {
        document.title = "Search <> Game Item Shop!";

        let uri = window.location.search.substring(1);
        let params = new URLSearchParams(uri);

        if (params.get("query")) {
            this.query = params.get("query");
            this.performSearch();
        }
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
        async performSearch() {
            this.$store.commit("setIsLoading", true);

            await axios
                .post("/api/v1/products/search/", { query: this.query })
                .then((response) => {
                    this.products = response.data;
                })
                .catch((error) => {
                    console.log(error);
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
