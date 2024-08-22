from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.parses import JSONParser
from weasyprint import HTML

class GeneratePDFView(APIView):
    parser_classes = [JSONParser]

    # Remove a DjangoModelPermissionsOrAnonReadOnly se aplicada globalmente a remove localmente pois é desnecessária ja que a nescessidade é apenas gerar um PDF 
    permission_classes = []

    def get(self, request):
        # Recebe o template HMTL Via post
        html_content = request.data.get('html', '')

        # Gera o PDF usando HTML Recebido
        pdf = HTML(string=html_content).write_pdf()

        # Cria um objeto HttpResponse com o tipo de conteúdo PDF
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="report.pdf"'
        return response