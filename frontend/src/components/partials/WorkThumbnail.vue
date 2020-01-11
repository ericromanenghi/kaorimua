<template>
    <div class='work__item work__item--menu' v-if='isMenuItem'></div>
    <router-link v-else :to='workEnhanced.link' class='work__item' :style='workEnhanced.style'>{{ workEnhanced.title }}</router-link>
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

<style lang='scss' scoped>
@import './../../scss/variables.scss';

.work__item {
    align-items: center;
    background-color: $color-secondary;
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center center;
    color: #fff;
    display: flex;
    flex: 0 0 auto;
    font-size: 1.7em;
    height: calc(100vh - 164px);
    justify-content: center;
    margin-right: 10px;
    text-decoration: none;
    width: 300px;
}
.work__item--menu {
    display: none;
}

@media screen and (min-width: 700px) {
    .work__item {
        flex: 0 0 auto;
        font-size: 2.1em;
        font-weight: bold;
        height: calc(100vh - 30px);
        margin-right: 15px;
        width: 450px;
    }
    .work__item--menu {
        display: block;
        visibility: hidden;
        width: 300px;
    }
}
</style>