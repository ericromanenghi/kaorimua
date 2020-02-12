<template>
    <div class='container'>
        <div class='cover'>
            <div class='cover__photo' v-for='(photo, index) in photos' :key='photo' :style='{ backgroundImage: `url(${photo})`, opacity: currentPhotoIndex === index ? 1 : 0 }'></div>
            <div class='cover__text'>
                <h1>Kaori Yonamine<br>Professional MakeUp Artist</h1>
            </div>
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

<style scoped lang='scss' src='@/scss/cover.scss'></style>