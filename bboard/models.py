from django.db import models

class Rubric(models.Model):
	name = models.CharField("Название", max_length=20, db_index=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Рубрика"
		verbose_name_plural = "Рубрики"
		ordering = ["name"]


class Bd(models.Model):
	title = models.CharField("Товар", max_length=50)
	content = models.TextField("Описание", null=True, blank=True)
	price = models.FloatField("Цена", null=True, blank=True)
	published = models.DateTimeField("Опубликовано", auto_now_add=True, db_index=True)

	rubric = models.ForeignKey(Rubric, null=True,
								on_delete=models.PROTECT, verbose_name="Рубрика")


	class Meta:
		verbose_name = "Обьявление"
		verbose_name_plural = "Обьявления"
		ordering = ["-published"]




