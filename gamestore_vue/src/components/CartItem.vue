<template>
    <tr>
        <td class="has-text-left"><router-link :to="item.product.get_absolute_url">{{ item.product.name }}</router-link></td>
        <td class="has-text-left">${{ item.product.price }}</td>
        <td class="has-text-left">{{ item.product.salePercentAsDeci !==0 ? (item.product.salePercentAsDeci*100) + '%' : '0%' }}</td>
        <td class="has-text-left">
            {{ item.quantity }}
            <a @click="decrementQuantity(item)">-</a>
            <a @click="incrementQuantity(item)">+</a>
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