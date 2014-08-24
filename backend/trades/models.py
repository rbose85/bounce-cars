import datetime

from django.db import models


class Trade(models.Model):
    """
    A model to hold trade information - stored, per `symbol` per `time_stamp`.
    """

    SYM_LFZ = "LFZ"
    SYM_EURGBP = "EUR/GBP"
    SYM_6A = "6A"
    SYM_FDAX = "FDAX"

    SYMBOL_CHOICES = (
        (SYM_LFZ, "LFZ"),
        (SYM_EURGBP, "EUR/GBP"),
        (SYM_6A, "6A"),
        (SYM_FDAX, "FDAX"),
    )

    time_stamp = models.DateTimeField(
        verbose_name="Time Stamp", editable=False,
        default=datetime.datetime.now, blank=False)
    symbol = models.CharField(
        verbose_name="Symbol", editable=False, default="", blank=False,
        max_length=8, choices=SYMBOL_CHOICES)

    quote_count = models.IntegerField(
        verbose_name="Quote Count", editable=False, default=0, blank=False)
    trade_count = models.IntegerField(
        verbose_name="Trade Count", editable=False, default=0, blank=False)

    open_px = models.DecimalField(
        verbose_name="Open Px", editable=False, default=1.0, blank=False,
        max_digits=20, decimal_places=10)
    close_px = models.DecimalField(
        verbose_name="Close Px", editable=False, default=1.0, blank=False,
        max_digits=20, decimal_places=10)
    high_px = models.DecimalField(
        verbose_name="High Px", editable=False, default=1.0, blank=False,
        max_digits=20, decimal_places=10)
    low_px = models.DecimalField(
        verbose_name="Low Px", editable=False, default=1.0, blank=False,
        max_digits=20, decimal_places=10)

    # these two, `created` and `modified`, refer to the db record only
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        get_latest_by = "modified"
        ordering = ("time_stamp", "symbol", )
        unique_together = (("time_stamp", "symbol"),)
