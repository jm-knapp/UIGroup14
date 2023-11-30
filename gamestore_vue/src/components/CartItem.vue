<template>
    <tr>
        <td class="has-text-left"><router-link :to="item.product.get_absolute_url">{{ item.product.name }}</router-link></td>
        <td class="has-text-left">${{ item.product.price }}</td>
        <td class="has-text-left">{{ item.product.salePercentAsDeci !==0 ? (item.product.salePercentAsDeci*100) + '%' : '0%' }}</td>
        <td class="has-text-left">
            {{ item.quantity }}
            <button @click="decrementQuantity(item)" class="is-size-4 has-text-weight-bold" aria-label="Decrease quantity of item">
                <span class="extendMinus" aria-hidden="true">-</span>
            </button>
            <button @click="incrementQuantity(item)" class="is-size-4 has-text-weight-bold" aria-label="Increase quantity of item">
                <span class="extendMinus" aria-hidden="true">+</span>
            </button>
        </td>
        <td class="has-text-left">${{ getItemTotal(item).toFixed(2) }}</td>
        <td class="has-text-left"><button class="delete" @click="removeFromCart(item)"></button></td>
    </tr>
</template>

<script>
export default {
    name: 'CartItem',
    props: {
        initialItem: Object
    },
    data() {
        return {
            item: this.initialItem
        }
    },
    methods: {
        //Can probably modify the below for discounts
        getItemTotal(item) {
            if(item.product.salePercentAsDeci > 0){
                return item.quantity * item.product.price * (1-item.product.salePercentAsDeci)
            }else{
                return item.quantity * item.product.price
            }
            
        },
        decrementQuantity(item) {
            item.quantity -= 1

            if (item.quantity === 0) {
                this.$emit('removeFromCart', item)
            }

            this.updateCart()
        },
        incrementQuantity(item) {
            item.quantity += 1

            this.updateCart()
        },
        updateCart() {
            localStorage.setItem('cart', JSON.stringify(this.$store.state.cart))
        },
        removeFromCart(item) {
            this.$emit('removeFromCart', item)

            this.updateCart()
        },
    },
}
</script>

<style lang="scss">
    .extendMinus::before{
        content: "\00a0";
        display: inline-block;
    }
    .extendMinus::after{
        content: "\00a0";
    }
</style>