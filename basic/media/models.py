import json

from django.db import models
from django.conf import settings
from django.urls import reverse


class AudioSet(models.Model):
    """AudioSet model"""

    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True)
    audios = models.ManyToManyField('Audio', related_name='audio_sets')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'media_audio_sets'

    def __unicode__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return reverse('audio_set_detail', kwargs={'slug': self.slug})


class Audio(models.Model):
    """Audio model"""

    title = models.CharField(max_length=255)
    slug = models.SlugField()
    still = models.FileField(
        upload_to='audio_stills',
        blank=True,
        help_text='An image that will be used as a thumbnail.',
    )
    file = models.FileField(upload_to='audio')
    audio = models.FilePathField(
        path=settings.MEDIA_ROOT + "audios/",
        recursive=True,
        blank=True,
    )
    description = models.TextField(blank=True)
    uploaded = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'media_audio'
        verbose_name_plural = 'audios'

    def __unicode__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return reverse('audio_detail', kwargs={'slug': self.slug})


class PhotoSet(models.Model):
    """PhotoSet model"""

    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True)
    cover_photo = models.ForeignKey(
        'Photo', on_delete=models.CASCADE, blank=True, null=True
    )
    photos = models.ManyToManyField('Photo', related_name='photo_sets')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'media_photo_sets'

    def __unicode__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return reverse('photo_set_detail', kwargs={'slug': self.slug})


class PhotoManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset().filter(content_type=Photo.ContentType.PHOTO)
        )


class Photo(models.Model):
    """Photo model"""

    class ContentType(models.IntegerChoices):
        PHOTO = 1
        SCREENSHOT = 2
        ILLUSTRATION = 3

    LICENSES = (
        ('http://creativecommons.org/licenses/by/2.0/', 'CC Attribution'),
        (
            'http://creativecommons.org/licenses/by-nd/2.0/',
            'CC Attribution-NoDerivs',
        ),
        (
            'http://creativecommons.org/licenses/by-nc-nd/2.0/',
            'CC Attribution-NonCommercial-NoDerivs',
        ),
        (
            'http://creativecommons.org/licenses/by-nc/2.0/',
            'CC Attribution-NonCommercial',
        ),
        (
            'http://creativecommons.org/licenses/by-nc-sa/2.0/',
            'CC Attribution-NonCommercial-ShareAlike',
        ),
        (
            'http://creativecommons.org/licenses/by-sa/2.0/',
            'CC Attribution-ShareAlike',
        ),
    )

    objects = PhotoManager()

    title = models.CharField(max_length=255)
    slug = models.SlugField()
    photo = models.FileField(upload_to="photos")
    taken_by = models.CharField(max_length=100, blank=True)
    license = models.URLField(blank=True, choices=LICENSES)
    description = models.TextField(blank=True)
    uploaded = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    _exif = models.TextField(blank=True)
    content_type = models.IntegerField(choices=ContentType.choices, default=1)

    class Meta:
        db_table = 'media_photos'
        ordering = ('-uploaded',)

    def _set_exif(self, d):
        self._exif = json.dumps(d)

    def _get_exif(self):
        if self._exif:
            return json.loads(self._exif)
        else:
            return {}

    exif = property(_get_exif, _set_exif, "Photo EXIF data, as a dict.")

    def __unicode__(self):
        return '%s' % self.title

    @property
    def url(self):
        return '{}{}'.format(settings.MEDIA_URL, self.photo)

    def get_absolute_url(self):
        return reverse('photo_detail', kwargs={'slug': self.slug})


class ScreenshotManager(models.Manager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(content_type=Photo.ContentType.SCREENSHOT)
        )


class Screenshot(Photo):
    class Meta:
        proxy = True

    objects = ScreenshotManager()


class VideoSet(models.Model):
    """VideoSet model"""

    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True)
    videos = models.ManyToManyField('Video', related_name='video_sets')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'media_video_sets'

    def __unicode__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return reverse('video_set_detail', kwargs={'slug': self.slug})


class Video(models.Model):
    """Video model"""

    title = models.CharField(max_length=255)
    slug = models.SlugField()
    still = models.FileField(
        upload_to='video_stills',
        blank=True,
        help_text='An image that will be used as a thumbnail.',
    )
    file = models.FileField(upload_to='videos')
    video = models.FilePathField(
        path=settings.MEDIA_ROOT + 'videos/',
        recursive=True,
        blank=True,
    )
    description = models.TextField(blank=True)
    uploaded = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'media_videos'

    def __unicode__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return reverse('video_detail', kwargs={"slug": self.slug})
