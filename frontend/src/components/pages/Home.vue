<template>
    <div class='container'>
        <div class='cover'>
            <div class='cover__photo' v-for='(photo, index) in photos' :key='photo' :style='{ backgroundImage: `url(${photo})`, opacity: currentPhotoIndex === index ? 1 : 0 }'></div>
        </div>
    </div>
</template>

<script>
export default {
    data () {
        return {
            photos: [
                `${process.env.BASE_URL}photos/home/photo-1.jpg`,
                `${process.env.BASE_URL}photos/home/photo-2.jpg`,
                `${process.env.BASE_URL}photos/home/photo-3.jpg`,
            ],
            currentPhotoIndex: 0,
            interval: null,
        }
    },

    methods: {
        changeImage () {
            ++this.currentPhotoIndex
            if (this.currentPhotoIndex >= this.photos.length) this.currentPhotoIndex = 0
        }
    },

    mounted () {
        this.interval = setInterval(this.changeImage, 5000)
    },

    destroyed () {
        clearInterval(this.interval)
        this.interval = null
    }
}
</script>

<style scoped lang='scss'>
@import './../../scss/variables.scss';

.cover {
    display: block;
    height: calc(100vh - 164px);
    margin: 10px;
    position: relative;
    width: calc(100% - 20px);
}
.cover__photo {
    background-position: center center;
    background-repeat: no-repeat;
    background-size: cover;
    height: 100%;
    left: 0;
    position: absolute;
    top: 0;
    transition: opacity .6s linear;
    width: 100%;
    z-index: 3;
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
    z-index: 4;
}

@media screen and (min-width: 700px) {
    .cover {
        height: calc(100vh - 30px);
        margin: 15px;
        width: calc(100% - 30px);
    }
}
</style>