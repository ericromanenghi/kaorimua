<template>
    <div class='work__item work__item--menu' v-if='isMenuItem'></div>
    <router-link v-else :to='workEnhanced.link' class='work__item' :style='workEnhanced.style'>
        <div>{{ workEnhanced.title }}</div>
    </router-link>
</template>

<script>
export default {
    props: [ 'work', 'isMenuItem' ],
    computed: {
        workEnhanced: function () {
            return {
                ...this.work,
                link: `/work/${this.work.slug}`,
                style: `background-image: url(${this.work.photo})`,
            }
        }
    }
}
</script>

<style lang='scss' src='@/scss/work/item.scss' scoped></style>
