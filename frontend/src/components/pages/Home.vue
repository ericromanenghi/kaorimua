<template>
    <div class='container'>
        <div class='cover'></div>
    </div>
</template>

<script>
export default {
    
}
</script>

<style scoped lang='scss'>
@import './../../scss/variables.scss';

.cover {
    background-image: url(/photos/home/photo.jpg);
    background-position: center center;
    background-repeat: no-repeat;
    background-size: cover;
    display: block;
    height: calc(100vh - 164px);
    margin: 10px;
    position: relative;
    width: calc(100% - 20px);
}
.cover:after {
    background: rgba($color-secondary, .5);
    content: '';
    display: block;
    height: 100%;
    left: 0;
    position: absolute;
    top: 0;
    width: 100%;
}

@media screen and (min-width: 700px) {
    .cover {
        height: calc(100vh - 30px);
        margin: 15px;
        width: calc(100% - 30px);
    }
}
</style>