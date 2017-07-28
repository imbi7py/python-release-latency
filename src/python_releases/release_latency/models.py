from django.db import models

class PythonImplementation(models.Model):
    """Collection of tracked Python implementations"""
    name = models.CharField(max_length=200)

class PythonRelease(models.Model):
    """Release details for tracked implementations"""
    class Meta:
        unique_together = ("implementation", "version")

    implementation = models.ForeignKey(PythonImplementation, on_delete=models.CASCADE)
    version = models.CharField(max_length=20)
    python_version = models.CharField(max_length=20)
    release_date = models.DateField("date released")

    _FULL_RELEASE = "full"
    _SOURCE_ONLY_RELEASE = "source"
    _RELEASE_KINDS = (
        (_FULL_RELEASE, "Full release"),
        (_SOURCE_ONLY_RELEASE, "Source-only release"),
    )
    kind = models.CharField(
        max_length=10,
        choices=_RELEASE_KINDS,
        default=_FULL_RELEASE,
    )
