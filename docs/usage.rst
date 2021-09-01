=====
Usage
=====

To use Django Clear S2S in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_clear_s2s.apps.DjangoClearS2sConfig',
        ...
    )

Add Django Clear S2S's URL patterns:

.. code-block:: python

    from django_clear_s2s import urls as django_clear_s2s_urls


    urlpatterns = [
        ...
        url(r'^', include(django_clear_s2s_urls)),
        ...
    ]
